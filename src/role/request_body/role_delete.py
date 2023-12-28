from rest_framework import serializers

class RoleDelete(serializers.Serializer):
    id = serializers.IntegerField()