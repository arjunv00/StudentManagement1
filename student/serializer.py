
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Student


# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):

        return User.objects.create_user(
            **validated_data
        )


# STUDENT SERIALIZER
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id"]
