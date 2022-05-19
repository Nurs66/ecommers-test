from django.urls import path
from apps.trade_points import views

urlpatterns = [
    path('', views.TradePointListAPIView.as_view(), name='trade_points'),
]

