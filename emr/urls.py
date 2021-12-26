from django.urls import path
from emr.views.patient.patientCount import PatientAllView, PatientGenderView,\
    PatientRaceView, PatientEthnicityView, PatientDeathView
from emr.views.visit.visitCount import VisitTypeView, VisitGenderView, VisitRaceView,\
    VisitEthnicityView, VisitAgeGroupView
from emr.views.concept.conceptInfo import ConceptDetailView
from emr.views.concept.personInfo import PersonGenderConceptDetailView, PersonRaceDetailView, PersonEthnicityDetailView

urlpatterns = [
    # 환자 관련
    path('patient/count/all/', PatientAllView.as_view()),               # 전체 환자 수
    path('patient/count/gender/', PatientGenderView.as_view()),         # 성별 환자 수
    path('patient/count/race/', PatientRaceView.as_view()),             # 인종별 환자 수
    path('patient/count/ethnicity/', PatientEthnicityView.as_view()),   # 민족별 환자 수
    path('patient/count/death/', PatientDeathView.as_view()),           # 사망 환자 수

    # 방문 관련
    path('visit/count/type/', VisitTypeView.as_view()),                 # 유형별 방문자 수
    path('visit/count/gender/', VisitGenderView.as_view()),             # 성별 방문자 수
    path('visit/count/race/', VisitRaceView.as_view()),                 # 인종별 방문자 수
    path('visit/count/ethnicity/', VisitEthnicityView.as_view()),       # 민족별 방문자 수
    path('visit/count/age/', VisitAgeGroupView.as_view()),              # 연령대(10세)별 방문자 수

    # concept 관련
    path('concept', ConceptDetailView.as_view()),                              # 전체 concept 정보 + ?page=$int, $search=$str
    path('concept/person/gender', PersonGenderConceptDetailView.as_view()),    # 환자 성별 concept 정보 + ?page=$int, $search=$str
    path('concept/person/race', PersonRaceDetailView.as_view()),               # 환자 인종별 concept 정보 + ?page=$int, $search=$str
    path('concept/person/ethnicity', PersonEthnicityDetailView.as_view())      # 환자 민족별 concept 정보 + ?page=$int, $search=$str

    # path('concept/visit/type/', ConceptDetailView.as_view())       # 방문자 유형별 concept 정보

    # path('concept/condition/', ConceptDetailView.as_view())       # 진단(병명) concept 정보

    # path('concept/drug/', ConceptDetailView.as_view())       # 처방 의약품 concept 정보



    # table row 관련
    # person 전체 read
    # visit_occurrence 전체 read
    # condition_occurrence 전체 read
    # drug_exposure 전체 read
    #
]
