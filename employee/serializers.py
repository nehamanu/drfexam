from rest_framework import serializers
from employee.models import Employee
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=['username',
                'password',
                'email',
                ]

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u