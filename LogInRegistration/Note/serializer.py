from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    '''This will serialize the complex data'''
    class Meta:
        model = Notes
        fields = ['id','title','description']