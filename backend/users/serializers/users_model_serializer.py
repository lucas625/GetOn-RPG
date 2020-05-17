"""Core app module for template model serializer."""

from rest_framework import serializers
from users.models import UserModel


class UsersModelSerializer(serializers.ModelSerializer):
    """
    Serializes the Template model.
    """

    class Meta:
        """Template Model Serializer meta class."""
        model = UserModel
        fields = '__all__'