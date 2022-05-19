from rest_framework.views import APIView
from rest_framework.response import Response
from apps.trade_points.models import TradePoint
from apps.trade_points.serializers import TradePointSerializer


class TradePointListAPIView(APIView):
    def get(self, request):
        queryset = TradePoint.objects.filter(
            employee__phone_number=self.request.query_params.get('phone'))
        serializer = TradePointSerializer(queryset, many=True)
        return Response(serializer.data)
