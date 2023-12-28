from rest_framework import serializers

class RoleList(serializers.Serializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    searchText = serializers.CharField(required=False)