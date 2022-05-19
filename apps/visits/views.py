from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import status
from apps.visits.serializers import VisitSerializer
from apps.visits.models import TradePoint


class VisitCreateAPIView(APIView):

    def post(self, request):
        serializer = VisitSerializer(data=request.data)
        trade_point = get_object_or_404(TradePoint, id=self.request.data.get('trade_point'))
        phone = self.request.query_params.get('phone')

        if serializer.is_valid():
            if phone:
                if phone == trade_point.employee.phone_number:
                    serializer.save(trade_point=trade_point)
                    return Response(serializer.data,
                                    status=status.HTTP_201_CREATED)
                else:
                    raise ValidationError({"error": "wrong employee's phone."})
            else:
                raise ValidationError({"error": "phone was not provided."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
