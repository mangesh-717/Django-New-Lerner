# Creating serializers here

# Serializer is used to convert this model data to serialized format, i.e., JSON

from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Uncomment and complete this if you need to serialize Employee model as well
# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'
