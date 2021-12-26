# Simple Emr API

This Project is for develop simple api server using EMR data generated virtually using Synthea into Common Data Model.

Using python3 & django rest-framework.

### DJANGO PROJECT

- simple_emr_api

### DJANGO APP 

- emr

# API List

It is simple api server. You can find api list to urls.py in each app.

No Credentials are needed.

| URL                          | METHOD | PARAM                                 |                  EXPLAINATION                   |                                                                                                 Sample Data                                                                                                 |
|:-----------------------------|:------:|:--------------------------------------|:-----------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| api/patient/count/all/       |  GET   | N/A                                   |                  전체 환자 수 가져오기                   |                                                                                               {"count":1000}                                                                                                |
| api/patient/count/gender/    |  GET   | N/A                                   |                  성별 환자 수 가져오기                   |                                                                                        {"FEMALE": 452, "MALE": 548}                                                                                         |
| api/patient/count/race/      |  GET   | N/A                                   |                  인종별 환자 수 가져오기                  |                                                           {"No matching concept": 4, "White": 845, "Black or African American": 86, "Asian": 65}                                                            |
| api/patient/count/ethnicity/ |  GET   | N/A                                   |                  민족별 환자 수 가져오기                  |                                                                                        {"No matching concept": 1000}                                                                                        |
| api/patient/count/death/     |  GET   | N/A                                   |                  사망 환자 수 가져오기                   |                                                                                               {"count": 152"}                                                                                               |
| api/visit/count/type/        |  GET   | N/A                                   |                방문 유형별 방문 수 가져오기                 |                                                             {"Emergency Room Visit": 3475, "Inpatient Visit": 1309, "Outpatient Visit": 37026}                                                              |
| api/visit/count/gender/      |  GET   | N/A                                   |                  성별 방문 수 가져오기                   |                                                                                      {"FEMALE": 19307, "MALE": 22503}                                                                                       |
| api/visit/count/race/        |  GET   | N/A                                   |                  인종별 방문 수 가져오기                  |                                                       {"Asian": 2826, "Black or African American": 3326, "No matching concept": 171, "White": 35487}                                                        |
| api/visit/count/ethnicity/   |  GET   | N/A                                   |                  민족별 방문 수 가져오기                  |                                                                                        {"No matching concept": 1000}                                                                                        |
| api/visit/count/age/         |  GET   | N/A                                   |           방문시 연령대(10세 단위)별 방문 수 가져오기            |                              {"60": 4995, "70": 4012, "50": 6141, "0": 1178, "10": 2366, "20": 3867, "80": 3621, "30": 3376, "40": 4167, "100": 4913, "90": 2621, "110": 553}                               |
 | api/concept                  |  GET   | page, search : ?page=$num&search=$str | 전체 concept 정보 (20개씩), search = concept_name을 검색 |                {"count": 7403692, "next": $url or null, "previous": $url or null, "results": [{"concept_id": 600000012, "concept_name": "OMOP Drug cohort era", "domain_id": "Drug"}, ...]}                 |
 | api/concept/person/gender    |  GET   | page, search : ?page=$num&search=$str |             환자 성별 concept 정보 (20개씩), search = concept_name을 검색             |     {"count": 2, "next": $url or null, "previous": $url or null, "results": [{"gender_concept__concept_id": 8507, "gender_concept__concept_name": "MALE", "gender_concept__domain_id": "Gender"}, ...]}     |
 | api/concept/person/race      |  GET   | page, search : ?page=$num&search=$str |            환자 인종별 concept 정보 (20개씩), search = concept_name을 검색             | {"count": 4, "next": $url or null, "previous": $url or null, "results": [{"race_concept__concept_id": 0, "race_concept__concept_name": "No matching concept", "race_concept__domain_id": "Metadata"}, ...]} |
 | api/concept/ethnicity        |  GET   | page, search : ?page=$num&search=$str |            환자 민족별 concept 정보 (20개씩), search = concept_name을 검색             | {"count": 1, "next": $url or null, "previous": $url or null, "results": [{"ethnicity_concept__concept_id": 0, "ethnicity_concept__concept_name": "No matching concept", "ethnicity_concept__domain_id": "Metadata"}, ...]} |

# Architecture
-
- Web Server : nginx 
- Interface(wsgi) : gunicorn 
- WAS : django 
- DB : postgresql (external regacy db)

# SET-UP

Please check this "SET-UP" contents before start this project.

## 0. Warning - Set Secrets

 > Before launch this server, you have to set settings.ini (simple_emr_api/settings.ini)

```
#settings.ini
[settings]
SECRET_KEY=your-secret-key 
POSTGRES_NAME=your-database-name 
POSTGRES_USER=your-database-user-id 
POSTGRES_PASSWORD=your-database-user-password 
POSTGRES_HOST=your-database-host
POSTGRES_PORT=your-database-port
```


## 1. Target OS

- ubuntu 18.04

## 2. Dependancy

- Dependancy List (in requirements.txt)

```
asgiref==3.4.1
backports.zoneinfo==0.2.1
Django==4.0
django-cors-headers==3.10.1
djangorestframework==3.13.1
psycopg2-binary==2.9.2
python-decouple==3.5
pytz==2021.3
sqlparse==0.4.2
```

## 3. How to set

- going to add init_sh.sh
```
    # 1. clone this project
    # 2. write your secrets in simple_emr_api/settings.ini
    # 3. Run with root authority or account
    set chmod 744 init_sh.sh 
    run init_sh.sh
```

# Test
    going to add this...
