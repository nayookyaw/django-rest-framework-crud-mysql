from django.db.models.query import QuerySet
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Role
from .serializers import RoleSerializer

class RoleRepositories():

    @classmethod
    def save_role(cls, role_serializer: RoleSerializer) -> Role | None:
        if role_serializer.is_valid():
            return role_serializer.save()
        return None
    
    @classmethod
    def update_role(cls, role_serializer: RoleSerializer) -> Role | None:
        if role_serializer.is_valid():
            return role_serializer.save()
        return None
    
    @classmethod
    def delete_role(cls, role: Role) -> None:
        role.delete()

    @classmethod
    def get_role_by_id(cls, id: int) -> Role | None:
        role: Role | None = None
        try:
            role = Role.objects.get(pk=id)
        except Role.DoesNotExist:
            role = None
        
        return role

    @classmethod
    def get_role_list(cls, offset: int, limit: int, search_text: str) -> ReturnDict:
        queryset: QuerySet = Role.objects.all()
        if search_text is not None:
            queryset = queryset.filter(name__icontains=search_text)
        resultset: QuerySet = queryset.order_by("-id")[offset:limit]
        roleList : RoleSerializer = RoleSerializer(instance=resultset, many=True)
        return roleList.data

    
    
