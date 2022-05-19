from rest_framework import serializers
from apps.trade_points.models import TradePoint
from apps.visits.serializers import VisitSerializer


class TradePointSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(read_only=True, many=True)

    class Meta:
        model = TradePoint
        fields = (
            'id',
            'title',
            'employee',
            'visits',
        )
