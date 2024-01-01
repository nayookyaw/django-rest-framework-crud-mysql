from rest_framework import serializers

class UserAdd(serializers.Serializer):
    username = serializers.CharField(
        max_length=50,
        error_messages={
            'required': 'name is required',
            'max_length': 'name cannot be exceed 50',
        }
    )
    password = serializers.CharField(
        max_length=50,
        error_messages={
            'required': 'password is required',
            'max_length': 'password cannot be exceed 50',
        }
    )
    email = serializers.EmailField(
        max_length=50,
        error_messages={
            'required': 'email is required',
            'max_length': 'email cannot be exceed 50',
        }
    )
    details = serializers.CharField(required=False, max_length=250, default="details")