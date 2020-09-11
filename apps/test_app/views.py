import logging

from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.test_app import serializers, models

logger = logging.getLogger(__name__)

User = get_user_model()


class FriendViewSet(viewsets.ModelViewSet):
    """
    引用信息
    """

    serializer_class = serializers.FriendSerializers

    authentication_classes = [JSONWebTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Friend.objects.all()
