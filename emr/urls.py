from django.urls import path
from emr.views.patient.patientCount import PatientAllView, PatientGenderView, PatientRaceView, PatientEthnicityView, PatientDeathView


urlpatterns = [
    path('all/', PatientAllView.as_view()),
    path('gender/', PatientGenderView.as_view()),
    path('race/', PatientRaceView.as_view()),
    path('ethnicity/', PatientEthnicityView.as_view()),
    path('death/', PatientDeathView.as_view()),
]
