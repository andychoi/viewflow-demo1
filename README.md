python -m venv .venv
    source .venv/bin/activate
iii. initialize virtual environment and install requirements from requirements.txt (
    pip install -r requirements.txt
iv. python manage.py makemigrations
v. python manage.py migrate

    python manage.py createsuperuser
    
vi. run server from base directory:

    python manage.py runserver 0.0.0.0:8001


vfOA
=========

vfOA is an OA demonstration system based on Viewflow, which can quickly realize data CURD and process processing, and can develop lightweight OA/CRM/ERP systems.

For more information, please refer to django-viewflow, django-materia
## Installation and Dependencies:

 django==1.11.7

 django-filter==1.1.0
 
 django-formtools==2.1
 
 django-material==1.1.1
 
 django-viewflow==1.1.0
 
## Quick start:
 pip install -r requirements.txt
 
 python manage.py runserver 8888

## Photos:
Edit interface
![Edit interface](https://raw.githubusercontent.com/htwenhe/vfOA/master/img/1.PNG)

list page
![List page](https://raw.githubusercontent.com/htwenhe/vfOA/master/img/2.PNG)

To-do matters
![TODO](https://raw.githubusercontent.com/htwenhe/vfOA/master/img/3.PNG)

Process processing
![Process processing](https://raw.githubusercontent.com/htwenhe/vfOA/master/img/4.PNG)

Process information display
![Process information display](https://raw.githubusercontent.com/htwenhe/vfOA/master/img/5.PNG)