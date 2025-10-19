from rest_framework import generics, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from .serializers import RegisterSerializer, TicketSerializer
from .models import Ticket
from .permissions import IsOwnerOrAssigneeOrStaff

User = get_user_model()


# ✅ USER REGISTRATION VIEW
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ✅ LOGOUT VIEW
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=205)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


# ✅ TICKET VIEWSET (Full CRUD + Filtering + Search)
class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAssigneeOrStaff]
    queryset = Ticket.objects.filter(is_active=True).select_related(
        'department', 'category', 'created_by', 'assigned_to'
    ).order_by('-created_at')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'department', 'category', 'created_by', 'assigned_to']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'priority', 'status']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        # Soft delete instead of hard delete
        instance.is_active = False
        instance.save()
        
    def perform_update(self, serializer):
        # If assigned_to is being changed and current user is not staff, prevent it
        if 'assigned_to' in serializer.validated_data:
            if not self.request.user.is_staff:
                # remove assigned_to change, so only staff can assign
                serializer.validated_data.pop('assigned_to', None)
        serializer.save()
