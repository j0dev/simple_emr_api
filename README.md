# Simple Emr API

This Project is for develop simple api server using EMR data generated virtually using Synthea into Common Data Model.

Using python3 & django rest-framework.

### DJANGO PROJECT

- simple_emr_api

### DJANGO APP 

- emr

### REF

- https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:common_data_model

# API List

It is simple api server. You can find api list to urls.py in each app.

No Credentials are needed.

| URL                         | METHOD | PARAM                                                                 |                     EXPLAINATION                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Sample Data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------------------|:------:|:----------------------------------------------------------------------|:----------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| api/patient/count/all       |  GET   | N/A                                                                   |                     ?????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"count":1000}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| api/patient/count/gender    |  GET   | N/A                                                                   |                     ?????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"FEMALE": 452, "MALE": 548}                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| api/patient/count/race      |  GET   | N/A                                                                   |                    ????????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                               {"No matching concept": 4, "White": 845, "Black or African American": 86, "Asian": 65}                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| api/patient/count/ethnicity |  GET   | N/A                                                                   |                    ????????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"No matching concept": 1000}                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| api/patient/count/death     |  GET   | N/A                                                                   |                     ?????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"count": 152"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| api/patient/detail          |  GET   | page, search : $url?page=$num&search=$str                             | ?????? ?????? ?????? ????????? (20??????),  search = concept_name(??????)??? ??????  |                                                                                                                                                                                                                                                                     {"count": 1000, "next": $url or null, "previous": $url or null, "results": [{"person_id": 2804531,"gender_concept": {"concept_id": 8507, "concept_name": "MALE", "domain_id": "Gender"}, "birth_datetime": "2013-07-12T00:00:00+09:00", "race_concept": {"concept_id": 8527, "concept_name": "White", "domain_id": "Race"}, "ethnicity_concept": {"concept_id": 0, "concept_name": "No matching concept", "domain_id": "Metadata"}}, ...]}                                                                                                                                                                                                                                                                      |
| api/visit/count/type        |  GET   | N/A                                                                   |                   ?????? ????????? ?????? ??? ????????????                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"Emergency Room Visit": 3475, "Inpatient Visit": 1309, "Outpatient Visit": 37026}                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| api/visit/count/gender      |  GET   | N/A                                                                   |                     ?????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"FEMALE": 19307, "MALE": 22503}                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| api/visit/count/race        |  GET   | N/A                                                                   |                    ????????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                           {"Asian": 2826, "Black or African American": 3326, "No matching concept": 171, "White": 35487}                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| api/visit/count/ethnicity   |  GET   | N/A                                                                   |                    ????????? ?????? ??? ????????????                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"No matching concept": 1000}                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| api/visit/count/age         |  GET   | N/A                                                                   |              ????????? ?????????(10??? ??????)??? ?????? ??? ????????????              |                                                                                                                                                                                                                                                                                                                                                                                                                  {"60": 4995, "70": 4012, "50": 6141, "0": 1178, "10": 2366, "20": 3867, "80": 3621, "30": 3376, "40": 4167, "100": 4913, "90": 2621, "110": 553}                                                                                                                                                                                                                                                                                                                                                                                                                   |
| api/visit/detail            |  GET   | page, search : $url?page=$num&search=$str                                                                      |  ????????? ?????? ?????? (20??????), search = concept_name(????????????)??? ??????   |                                                                                                                                                                                                                                                                                   {{"count": 41810,"next": $url or null, "previous": $url or null, "results": [{"visit_occurrence_id": 134695719, "person": {"person_id": 624763, "birth_datetime": "2004-10-14T00:00:00+09:00"}, "visit_concept": {"concept_id": 9202, "concept_name": "Outpatient Visit", "domain_id": "Visit"}, "visit_start_datetime": "2016-11-02T15:38:11+09:00", "visit_end_datetime": "2016-11-02T16:08:11+09:00"}, ...]}                                                                                                                                                                                                                                                                                   |
 | api/concept                 |  GET   | page, search : $url?page=$num&search=$str                             |   ?????? concept ?????? (20??????), search = concept_name??? ??????    |                                                                                                                                                                                                                                                                                                                                                                                                    {"count": 7403692, "next": $url or null, "previous": $url or null, "results": [{"concept_id": 600000012, "concept_name": "OMOP Drug cohort era", "domain_id": "Drug"}, ...]}                                                                                                                                                                                                                                                                                                                                                                                                     |
 | api/concept/person/gender   |  GET   | page, search : $url?page=$num&search=$str                             |  ?????? ?????? concept ?????? (20??????), search = concept_name??? ??????  |                                                                                                                                                                                                                                                                                                                                                                                         {"count": 2, "next": $url or null, "previous": $url or null, "results": [{"gender_concept__concept_id": 8507, "gender_concept__concept_name": "MALE", "gender_concept__domain_id": "Gender"}, ...]}                                                                                                                                                                                                                                                                                                                                                                                         |
 | api/concept/person/race     |  GET   | page, search : $url?page=$num&search=$str                             | ?????? ????????? concept ?????? (20??????), search = concept_name??? ??????  |                                                                                                                                                                                                                                                                                                                                                                                     {"count": 4, "next": $url or null, "previous": $url or null, "results": [{"race_concept__concept_id": 0, "race_concept__concept_name": "No matching concept", "race_concept__domain_id": "Metadata"}, ...]}                                                                                                                                                                                                                                                                                                                                                                                     |
 | api/concept/ethnicity       |  GET   | page, search : $url?page=$num&search=$str                             | ?????? ????????? concept ?????? (20??????), search = concept_name??? ??????  |                                                                                                                                                                                                                                                                                                                                                                             {"count": 1, "next": $url or null, "previous": $url or null, "results": [{"ethnicity_concept__concept_id": 0, "ethnicity_concept__concept_name": "No matching concept", "ethnicity_concept__domain_id": "Metadata"}, ...]}                                                                                                                                                                                                                                                                                                                                                                              |
 | api/concept/visity/type     |  GET   | page, search : $url?page=$num&search=$str                             | ????????? ????????? concept ?????? (20??????), search = concept_name??? ?????? |                                                                                                                                                                                                                                                                                                                                                                                     {"count": 3, "next": $url or null, "previous": $url or null, "results": [{"visit_concept__concept_id": 9201, "visit_concept__concept_name": "Inpatient Visit", "visit_concept__domain_id": "Visit"}, ...]}                                                                                                                                                                                                                                                                                                                                                                                      |
 | api/concept/condition       |  GET   | page, search : $url?page=$num&search=$str                             | ??????(??????) concept ?????? (20??????), search = concept_name??? ??????  |                                                                                                                                                                                                                                                                                                                                                                            {"count": 151, "next": $url or null, "previous": $url or null, "results": [{"condition_concept__concept_id": 0, "condition_concept__concept_name": "No matching concept", "condition_concept__domain_id": "Metadata"}, ...]}                                                                                                                                                                                                                                                                                                                                                                             |
 | api/concept/drug            |  GET   | page, search : $url?page=$num&search=$str                             |  ?????? ?????? concept ?????? (20??????), search = concept_name??? ??????  |                                                                                                                                                                                                                                                                                                                                                                                    {"count": 164, "next": $url or null, "previous": $url or null, "results": [{"drug_concept__concept_id": 0, "drug_concept__concept_name": "No matching concept", "drug_concept__domain_id": "Metadata"}, ...]}                                                                                                                                                                                                                                                                                                                                                                                    |
| api/condition/detail            |  GET   | page, search : $url?page=$num&search=$str                             |   ?????? (??????) ?????? ??????, search = concept_name (?????? ??????)??? ??????   |                                                                                                                                                                                                        {"count": 12167, "next": $url or null, "previous": $url or null, "results": [{"condition_occurrence_id": 35829674, "person": {"person_id": 2843890, "birth_datetime": "1966-04-01T00:00:00+09:00"}, "condition_concept": {"concept_id": 437390, "concept_name": "Hypoxemia", "domain_id": "Condition"}, "condition_start_datetime": "2020-03-08T00:00:00+09:00", "condition_end_datetime": null, "visit_occurrence": {"visit_occurrence_id": 2800532, "visit_start_datetime": "2020-03-08T03:59:43+09:00", "visit_end_datetime": "2020-03-19T10:16:43+09:00"}}, ...]}                                                                                                                                                                                                        |
| api/drug/detail            |  GET   | page, search : $url?page=$num&search=$str                             |   ????????? ????????? ?????? ??????, search = concept_name (????????? ???)??? ??????   |                                                                                                                                                                             {"count": 46579,"next": $url or null, "previous": $url or null, "results": [{"drug_exposure_id": 148347855, "drug_concept": {"concept_id": 40213154, "concept_name": "Influenza, seasonal, injectable, preservative free", "domain_id": "Drug"}, "drug_exposure_start_datetime": "2013-11-08T03:28:43+09:00", "drug_exposure_end_datetime": "2013-11-08T03:28:43+09:00", "visit_occurrence": {"visit_occurrence_id": 53527560, "visit_start_datetime": "2013-11-08T03:28:43+09:00", "visit_end_datetime": "2013-11-08T03:43:43+09:00"}}, ...]}                                                                                                                                                                             |

# Architecture
- Web Server : nginx 
- Interface(wsgi) : gunicorn 
- WAS : django 
- DB : postgresql (external regacy db)
- Port : 80, 5432

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

- Ubuntu Server 20.04 LTS

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
    # -- if possible, edit the secrets logic to environment variable
    # 3. Run with root authority or account
    
    set chmod 744 init_sh.sh 
    run init_sh.sh
    
    # delete init_sh.sh when finish init_sh.sh 
```

# Test
    test! :D -->> http://$your_server_ip/api/patient/count/all
    


## ?????? ??? ##

- http://$your_server_ip/api/patient/count/all

- http://$your_server_ip/api/patient/count/gender

- http://$your_server_ip/api/patient/count/race

- http://$your_server_ip/api/patient/count/ethnicity

- http://$your_server_ip/api/patient/count/death

## ?????? ?????? ?????? ##

- http://$your_server_ip/api/patient/detail?page=1&search=

## ?????? ??? ##

- http://$your_server_ip/api/visit/count/type

- http://$your_server_ip/api/visit/count/gender

- http://$your_server_ip/api/visit/count/race

- http://$your_server_ip/api/visit/count/ethnicity

- http://$your_server_ip/api/visit/count/age

## ?????? ?????? ?????? ##

- http://$your_server_ip/api/visit/detail?page=1&search=

## concept ?????? ##

- http://$your_server_ip/api/concept?page=1&search=

- http://$your_server_ip/api/concept/person/gender?page=1&search=

- http://$your_server_ip/api/concept/person/race?page=1&search=

- http://$your_server_ip/api/concept/person/ethnicity?page=1&search=

- http://$your_server_ip/api/concept/visit/type?page=1&search=

- http://$your_server_ip/api/concept/condition?page=1&search=

- http://$your_server_ip/api/concept/drug?page=1&search=

## ??????(??????) ???????????? ##

- http://$your_server_ip/api/condition/detail?page=1&search=

## ?????? ????????? ?????? ?????? ##

- http://$your_server_ip/api/drug/detail?page=1&search=


