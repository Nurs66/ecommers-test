from django.urls import path
from apps.visits import views

urlpatterns = [
    path('', views.VisitCreateAPIView.as_view(), name='visits'),
]