from rest_framework.views import APIView
from rest_framework.response import Response

from termcolor import colored

from ..constants.global_constants import GlobalConstants
from ..utils.response_util import ResponseUtil

from .services import Services
from .repositories import Repositories
from .serializers import RoleSerializer

# add, update, delete
class RoleView(APIView):
    def get(self, request, pk:int) -> Response:
        try:
            return Services.get_role_by_id(id=pk)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))
    
    def post(self, request, pk:int) -> Response:
        try:
            return Services.save_role(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))

    def put(self, request, pk:int) -> Response:
        try:
            return Services.update_role(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))


# list
class RoleListView(APIView):
    def post(self, request) -> Response:
        try:            
            return Services.get_list_role(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))

