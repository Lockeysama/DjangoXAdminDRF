from rest_framework import serializers

from apps.test_app import models


class FriendSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = '__all__'
