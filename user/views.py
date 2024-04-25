from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.services import registerUser


class RegistrationView(APIView):
    def post(self, request):
        response = registerUser(request)
        return response
