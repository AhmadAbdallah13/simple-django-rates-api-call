from django.urls import path
from .views import rates_view #RatesCreateView 

urlpatterns = [
    path('', rates_view, name='rates'),
    # path('', RatesCreateView.as_view(), name='rates'),
]