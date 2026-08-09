from rest_framework import serializers
from django.contrib.auth.models import Group, User
from kpi.models import Asset


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class NexusFormSerializer(serializers.ModelSerializer):
    has_deployment = serializers.SerializerMethodField()
    settings = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ['uid', 'name', 'settings', 'has_deployment']

    def get_has_deployment(self, obj):
        return True

    def get_settings(self, obj):
        return {
            'description': obj.settings.get('description', ''),
        }
