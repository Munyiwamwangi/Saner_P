from rest_framework import serializers

from .models import LeaveClassDetails, LeaveModels, LeaveType


class LeaveClassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveClassDetails
        fields = '__all__'

class EmploymentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModels
        fields = '__all__'
