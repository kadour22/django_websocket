from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAdminUser

from django.utils.crypto import get_random_string
from django.core.mail import send_mail

from .permissions import HumanResourcePermission
from .serializers import CreateEmployerSerializer
from .models import Employer

password = get_random_string(12)

class AddEmployerView(APIView) :
    permission_classes = [HumanResourcePermission | IsAdminUser]
    
    def post(self, request, *args, **kwargs) :
        serializer = CreateEmployerSerializer(data=request.data)
        if serializer.is_valid() :
            employer = serializer.save(password=password)
            return Response(serializer.data, status=201)
        return Response(serializer.errors , status=404)

