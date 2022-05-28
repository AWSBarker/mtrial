from django.urls import path
from .views import webhook, PairingsCreateView, PairingsListView, \
    MeasurementsListView, PatientsListView, DashBoard, DevicesListView

app_name = 'itasc'
urlpatterns = [
    path('', DashBoard.as_view(), name='dashboard'),
    path('bp/', webhook, name = 'webhook'),
    path('measures/', MeasurementsListView.as_view(), name='measurements-list'),
    path('patients/', PatientsListView.as_view(), name='patients-list'),
    path('pairings/', PairingsListView.as_view(), name='pairings-list'),
    path('pairings/create/', PairingsCreateView.as_view(), name='pairings-create'),
    path('devices/', DevicesListView.as_view(), name='devices-list'),
]

