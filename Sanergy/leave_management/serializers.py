#Serializing leave data for posting to salesforce
from rest_framework import serializers

from .models import LeaveClassDetails, LeaveType


class LeaveClassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveClassDetails

class EmploymentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
from rest_framework import serializers
from .models import LeaveModels



class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModels
        fields = '__all__'
