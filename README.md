# CS261-Project

Our Software Engineering (CS261) Project

Packages / Instructions:

- Navigate to base folder.
- Download Node.js and Python 3.9.
- Open 2 terminals.

Recommendation: use Conda to create a virtual environment.

In one:

- `python3 -m venv venv in one` or `conda create -n cs261 python=3.9`
- `pip install --user -r requirements.txt`
- `python backend/manage.py makemigrations`
- `python backend/manage.py migrate`
- `python backend/manage.py runserver`

in another:

- `cd ./frontend`
- `npm install react`
- `npm install --save react-circular-progressbar`
- `npm install axios`
- `npm start`
