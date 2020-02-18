from rest_framework import serializers

from .models import EmployeeLeaveRequest


class LeaveRequestsSerializer(serializers.ModelSerializer):
   class Meta:
      model = EmployeeLeaveRequest
      fields = '__all__'

from datetime import datetime
class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
