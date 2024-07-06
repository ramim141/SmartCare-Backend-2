from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    
    
    # custom query
    def get_queryset(self):
        return super().get_queryset()
        patient_id = self.request.query_params.get('patient_id') 
        if patient_id:
            queryset.filter(patient_id=patient_id)
        return queryset
    