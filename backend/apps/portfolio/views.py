import logging
from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

logger = logging.getLogger("apps")

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        try:
            return Project.objects.filter(owner=self.request.user)
        except Exception as exc:
            logger.exception("Error fetching projects: %s", exc)
            return Project.objects.none()

    def perform_create(self, serializer):
        logger.info("Creating project for %s", self.request.user)
        serializer.save(owner=self.request.user)
