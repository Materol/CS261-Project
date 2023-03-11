# CS261-Project

Our Software Engineering (CS261) Project

Packages / Instructions:

- Navigate to base folder
- open 2 terminals

Recommendation: use Conda to create a virtual environment.

In one:

- `python3 -m venv venv in one` or `conda create -n cs261 python=3.9`
- `pip install django djangorestframework djangorestframework-simplejwt django-rest-auth django-allauth django-cors-headers`
- `pip install pyjwt==1.7.1`
- `pip install numpy`
- `pip install -U scikit-learn`
- `python backend/manage.py makemigrations`
- `python backend/manage.py migrate`
- `python backend/manage.py runserver`

in another:

- `cd ./frontend`
- `npm install react`
- `npm install --save react-circular-progressbar`
- `npm install axios`
- `npm start`
