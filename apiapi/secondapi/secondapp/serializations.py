from rest_framework import serializers
from .models import *


# if we want to serilize specific fields from foraign model
class ColorsSerialization(serializers.ModelSerializer):

    class Meta:
        model=Colors
        fields=['color_name','id']
        # fields='__all__'


# what is difference between depth and another seralizer class
        # -->when we create another serializer it gives more control to us when we want to show specific fields but in depth it serializes all the data which is different or specic model  
        

class StudentSerializing(serializers.ModelSerializer):
    color=ColorsSerialization()
    class Meta:
        model=Students
        fields='__all__'
        
        # depth keyword is use to all the data is displayed from given foraign key
        # depth=1



  
    def validate_name(self, value):
        special_chars = "!@#$%^&*(){}:',./[]|\\~`_-"

        # Check if the name contains special characters
        if any(char in special_chars for char in value):
            raise serializers.ValidationError("Name should not contain special characters.")

        return value

    def validate_age(self, value):
        # Check if age is greater than 18
        if value and value <= 18:
            raise serializers.ValidationError("Age should be greater than 18.")

        return value