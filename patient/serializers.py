from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Patient
        fields = '__all__' # ['id', 'name', 'email', 'message', 'created_at']