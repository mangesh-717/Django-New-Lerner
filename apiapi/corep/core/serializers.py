from rest_framework import serializers
from .models import *
class STudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'

        # fields=['name','age']  #it is used to give specific fields
        # exclude=['id']   #it is used to exclude specific fields

        
    # it is validation part for serilizing 
    def validatee(self,data):
        special_characters='!@#$%!><?{}[()_*&^%-]'
        if any( char in special_characters for char in data['name']):
            raise serializers.ValidationError('name canot contain special chars')
        
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greator than 18')
        
        return data 