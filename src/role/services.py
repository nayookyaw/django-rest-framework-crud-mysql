from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from typing import Any, Dict

from collections import OrderedDict
from datetime import datetime

from ..utils.response_util import ResponseUtil
from .request_body.role_add import RoleAdd
from .request_body.role_update import RoleUpdate
from .request_body.role_delete import RoleDelete
from .request_body.role_list import RoleList
from .serializers import RoleSerializer
from .repositories import Repositories
from .models import Role

class Services():
    
    @classmethod
    def get_role_by_id(cls, id:int) -> Response:
        role : Role | None = Repositories.get_role_by_id(id=id)
        if role is not None:
            role_serializer: RoleSerializer = RoleSerializer(instance=role)
            return ResponseUtil.custom_success_response(
                data=role_serializer.data,
                message="role has been retrieved successfully"
            )
        else:
            return ResponseUtil.custom_fail_response(
                message="role does not exist"
            )
    
    @classmethod
    def save_role(cls, request) -> Response:
        request_serializer: RoleAdd = RoleAdd(data=request.data)
        if request_serializer.is_valid():
            validated_data : Any = request_serializer.validated_data
            new_role : RoleSerializer = RoleSerializer(data=validated_data)
            Repositories.save_role(role_serializer=new_role)
            return ResponseUtil.custom_success_response(
                message="role has been saved successfully"
            )
        else:
            return ResponseUtil.custom_fail_response(
                message="validation failed"
            )
    
    @classmethod
    def update_role(cls, request) -> Response:
        request_serializer : RoleUpdate = RoleUpdate(data=request.data)
        if request_serializer.is_valid():
            validated_data : Any = request_serializer.validated_data
            
            exist_role : Role | None = Repositories.get_role_by_id(id=validated_data.get('id'))
            if exist_role is not None:
                update_role : RoleSerializer = RoleSerializer(instance=exist_role, data=validated_data)
                Repositories.update_role(role_serializer=update_role)
                return ResponseUtil.custom_success_response(
                    message="role has been updated successfully"
                )
            else:
                return ResponseUtil.custom_fail_response(
                    message="role does not exist"
                )
        else:
            return ResponseUtil.custom_fail_response(
                message="validation failed"
            )
    
    @classmethod
    def delete_role(cls, request) -> Response:
        request_serializer: RoleDelete = RoleDelete(data=request.data)
        if request_serializer.is_valid():
            validated_data : Any = request_serializer.validated_data
            
            exist_role : Role | None = Repositories.get_role_by_id(id=validated_data.get('id'))
            if exist_role is not None:
                exist_role.deleted_at = datetime.now()
                role_serializer: RoleSerializer = RoleSerializer(instance=exist_role)
                Repositories.update_role(role_serializer=role_serializer)
                return ResponseUtil.custom_success_response(
                    message="role has been deleted successfully"
                )
            else:
                return ResponseUtil.custom_fail_response(
                    message="role does not exist"
                )
        else:
            return ResponseUtil.custom_fail_response(
                message="validation failed"
            )
    
    @classmethod
    def get_list_role(cls, request) -> Response:
        request_serializer: RoleList = RoleList(data=request.data)
        
        if request_serializer.is_valid():
            validated_data: Any = request_serializer.validated_data
            offset: int = validated_data.get("offset")
            limit: int = validated_data.get("limit")
            search_text: str = validated_data.get("searchText")

            role_list: ReturnDict = Repositories.get_role_list(offset=offset, limit=limit, search_text=search_text)
            role_count: int = 1
            res_data: dict[str, ReturnDict | int] = {
                'list': role_list,
                'count': role_count,
            }
            return ResponseUtil.custom_success_response(
                data=res_data,
                message="role list has been retrieved successfully"
            )
        else:
            return ResponseUtil.custom_fail_response(
                message="validation failed"
            )
