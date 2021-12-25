from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from emr.models import VisitOccurrence


class VisitTypeView(APIView):
    permission_classes = [AllowAny]
    # 방문 유형별 방문 수

    def get(self, request):
        queryset = VisitOccurrence.objects.select_related('visit_concept').values('visit_concept__concept_name') \
            .annotate(count=Count('visit_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('visit_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class VisitGenderView(APIView):
    permission_classes = [AllowAny]
    # 성별 방문 수

    def get(self, request):
        queryset = VisitOccurrence.objects.select_related('person').select_related('person__gender_concept').values('person__gender_concept__concept_name')\
            .annotate(count=Count('person__gender_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('person__gender_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class VisitRaceView(APIView):
    permission_classes = [AllowAny]
    # 인종별 방문 수

    def get(self, request):
        queryset = VisitOccurrence.objects.select_related('person').select_related('person__race_concept').values('person__race_concept__concept_name') \
            .annotate(count=Count('person__race_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('person__race_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class VisitEthnicityView(APIView):
    permission_classes = [AllowAny]
    # 민족별 방문자 수
    # ethnicity_concept_id 가 모두 0이고 concept_id가 0인 엔티티의 concept_name value가 "No matching concept"

    def get(self, request):
        queryset = VisitOccurrence.objects.select_related('person').select_related('person__ethnicity_concept').values('person__ethnicity_concept__concept_name') \
            .annotate(count=Count('person__ethnicity_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('person__ethnicity_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)


class VisitAgeGroupView(APIView):
    permission_classes = [AllowAny]
    # 민족별 방문자 수
    # ethnicity_concept_id 가 모두 0이고 concept_id가 0인 엔티티의 concept_name value가 "No matching concept"

    def get(self, request):
        queryset = VisitOccurrence.objects.select_related('person').select_related('person__ethnicity_concept').values('person__ethnicity_concept__concept_name') \
            .annotate(count=Count('person__ethnicity_concept__concept_name'))

        # count data serializing
        res_data = {}
        for x in queryset:
            res_data[x.get('person__ethnicity_concept__concept_name')] = x.get('count')

        return Response(res_data, status=status.HTTP_200_OK)