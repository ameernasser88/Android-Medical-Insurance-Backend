from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hospitals',HospitalAPI)
router.register(r'clinics',ClinicAPI)
urlpatterns = [
]
urlpatterns+= router.urls