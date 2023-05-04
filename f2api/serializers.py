from rest_framework import serializers
from f2api.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields= ['id','folder_name', 'file']
    