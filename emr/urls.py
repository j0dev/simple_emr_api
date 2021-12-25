from django.urls import path
from emr.views.patient.patientCount import PatientAllView, PatientGenderView, PatientRaceView, PatientEthnicityView, PatientDeathView
from emr.views.visit.visitCount import VisitTypeView, VisitGenderView, VisitRaceView, VisitEthnicityView, VisitAgeGroupView


urlpatterns = [
    # 환자 관련
    path('patient/all/', PatientAllView.as_view()),
    path('patient/gender/', PatientGenderView.as_view()),
    path('patient/race/', PatientRaceView.as_view()),
    path('patient/ethnicity/', PatientEthnicityView.as_view()),
    path('patient/death/', PatientDeathView.as_view()),

    # 방문 관련
    path('visit/type/', VisitTypeView.as_view()),
    path('visit/gender/', VisitGenderView.as_view()),
    path('visit/race/', VisitRaceView.as_view()),
    path('visit/ethnicity/', VisitEthnicityView.as_view()),
    path('visit/age/', VisitAgeGroupView.as_view()),

    # concept 관련
    # concept의 domain_id 정보를 받아오는 url
    # concetp의 search 없이 보는 api (pagination) -> 정렬 기준 : concept_id 기준
    # concetp의 search가 가능한 api (pagination)

    # table row 관련
    # person 전체 read
    # visit_occurrence 전체 read
    # condition_occurrence 전체 read
    # drug_exposure 전체 read
    #
]
