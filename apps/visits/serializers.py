from rest_framework import serializers
from apps.visits.models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = (
            'id',
            'trade_point',
            'latitude',
            'longitude',
            'create_at',
        )
