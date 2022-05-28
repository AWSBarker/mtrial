from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from itasc.serializers import MeasurementsSerializer
from itasc.models import Measurements, Devices, Patients
from flatdict import FlatDict
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from itasc.models import Patients, Pairings
from django.urls import reverse_lazy
from itasc.forms import PairingsForm

class DashMixin(object):
    ''' adds context from all models to dashboard template '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Nmeasures'] = Measurements.objects.all().count()
        context['Ndevices'] = Devices.objects.all().count()
        context['Npatients'] = Patients.objects.all().count()
        context['Npairings'] = Pairings.objects.all().count()
        context['last_measures'] = Measurements.objects.all().order_by('-measurements_timestamp')[:10]
        context['Lpairs'] = Pairings.objects.all()
        return context

class MeasurementsListView(DashMixin, ListView):
    model = Measurements
    fields = ["measurements_timestamp" ,  "device_imei" , "patientid"]
    template_name = 'itasc/measurements_list.html'
    paginate_by = 30

class PairingsCreateView(DashMixin, SuccessMessageMixin, CreateView):
    model = Pairings
    form_class = PairingsForm
    #fields = ['subject', 'device']
    success_url = reverse_lazy('itasc:pairings-list')
    success_message = 'Added pairing  %(subject) '
    template_name = 'itasc/pairings_create.html'

class PatientsListView(DashMixin, ListView):
    model = Patients
    template_name = 'itasc/patients_list.html'

class DashBoard(DashMixin, ListView):
    context_object_name = 'dash_list'
    template_name = 'itasc/home.html'
    queryset = ''

class PairingsListView(DashMixin, ListView):
    model = Pairings
    template_name = 'itasc/pairings_list.html'

class DevicesListView(DashMixin, ListView):
    model = Devices
    template_name = 'itasc/devices_list.html'

@api_view(['POST'])
@csrf_exempt
def webhook(request):

    if request.method == 'GET':
        last10 = Measurements.objects.all() # [:5] .latest()
        serializer = MeasurementsSerializer(last10, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = FlatDict(JSONParser().parse(request), delimiter='_')
        data['metadata_deviceGroups'] = "N/A"
        post = Measurements()
        for (k,v) in data.items():
            print(f'post field is {k}, value is {v}')
            if v in ('true', 'True', 1, True):
                v = True
            if v in ('false', 'False', 0, False):
                v = False
            setattr(post, k.lower(), v) # post.device_imei = data['device_IMEI']
        post.save()
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
