from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """Application Serializer"""

    class Meta:
        model = Application
        fields = ('__all__')
