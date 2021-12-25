from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from emr.models.person import Person
from emr.models.death import Death


class PatientAllView(APIView):
    permission_classes = [AllowAny]
    # 전체 환자 수

    def get(self, request):
        queryset = Person.objects.all().count()
        return Response({"count": queryset}, status=status.HTTP_200_OK)


class PatientGenderView(APIView):
    permission_classes = [AllowAny]
    # 성별 환자 수

    def get(self, request):
        queryset = Person.objects.select_related('gender_concept').values('gender_concept__concept_name')\
            .annotate(count=Count('gender_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('gender_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class PatientRaceView(APIView):
    permission_classes = [AllowAny]
    # 인종별 환자 수

    def get(self, request):
        queryset = Person.objects.select_related('race_concept').values('race_concept__concept_name') \
            .annotate(count=Count('race_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('race_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class PatientEthnicityView(APIView):
    permission_classes = [AllowAny]
    # 민족별 환자 수
    # ethnicity_concept_id 가 모두 0이고 concept_id가 0인 엔티티의 concept_name value가 "No matching concept"


    def get(self, request):
        queryset = Person.objects.select_related('ethnicity_concept').values('ethnicity_concept__concept_name') \
            .annotate(count=Count('ethnicity_concept__concept_name'))

        # count data serializing
        res_data = {}

        for x in queryset:
            res_data[x.get('ethnicity_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class PatientDeathView(APIView):
    permission_classes = [AllowAny]
    # 사망 환자 수

    def get(self, request):
        queryset = Death.objects.all().count()
        return Response({"count": queryset}, status=status.HTTP_200_OK)