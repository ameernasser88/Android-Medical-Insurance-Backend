from rest_framework import status , viewsets
from .models import *
from .serializers import *

class HospitalAPI(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class ClinicAPI(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer