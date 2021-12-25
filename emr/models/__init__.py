from emr.models.person import Person
from emr.models.visitOccurrence import VisitOccurrence
from emr.models.conditionOccurrence import ConditionOccurrence
from emr.models.drugExposure import DrugExposure
from emr.models.concept import Concept
from emr.models.clinicalNote import ClinicalNote
from emr.models.drugPair import DrugPair


# 각 모델은 레거시 DB와 연결하기 때문에 inspectdb로 생성한 모델
# 한 클래스 내에서 동일한 ForeignKey 클래스를 여러번 호출하는 경우 related_name='$관계클래스_$대상클래스_%0d' 형식으로 지정

__all__ = [Person, VisitOccurrence, ConditionOccurrence, DrugExposure, Concept, ClinicalNote, DrugPair]
