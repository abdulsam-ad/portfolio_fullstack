import logging
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

logger = logging.getLogger("apps")

User = get_user_model()

class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        logger.info("Fetching profile for user %s", self.request.user)
        try:
            return self.request.user
        except Exception as exc:  # broad but for demo
            logger.exception("Failed to get user: %s", exc)
            raise
