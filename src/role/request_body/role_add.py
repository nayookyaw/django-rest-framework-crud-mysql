from rest_framework import serializers

class RoleAdd(serializers.Serializer):
    name = serializers.CharField(
        max_length=20,
        error_messages={
            'required': 'name is required',
            'max_length': 'name cannot be exceed 2',
        }
    )
    details = serializers.CharField(required=False, max_length=250)
    remark = serializers.CharField(required=False, max_length=250)
    createdUser = serializers.CharField(required=False, max_length=250)