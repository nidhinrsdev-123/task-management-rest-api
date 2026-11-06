from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
from .permissions import IsOwnerOrStaff
from .serializers import RegisterSerializer,TaskSerializer
class RegisterView(generics.CreateAPIView):
 serializer_class=RegisterSerializer; permission_classes=[AllowAny]
class TaskViewSet(viewsets.ModelViewSet):
 serializer_class=TaskSerializer; permission_classes=[IsAuthenticated,IsOwnerOrStaff]
 filterset_fields=["status","priority"]; search_fields=["title","description"]; ordering_fields=["created_at","due_date","priority"]
 def get_queryset(self):
  qs=Task.objects.select_related("owner")
  return qs if self.request.user.is_staff else qs.filter(owner=self.request.user)
 def perform_create(self,serializer): serializer.save(owner=self.request.user)
