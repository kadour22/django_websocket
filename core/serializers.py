from rest_framework import serializers
from .models import Employer

class CreateEmployerSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Employer
        fields = [
            'first_name',
            'last_name',
            'email',     
            'position',  
            'rank'      
        ]
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Employer(**validated_data)
        if password:
            user.set_password(password)   # ✅ hashes the password
        user.save()
        return user
