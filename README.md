# Restaurant kitchen service

Django project for managing dish types, dishes and cooks in Restaurant

## Check it out!

[Restaurant project deployed to Render](https://restaurant-kitchen-service-l32g.onrender.com/)

login: admin
password: admin

## Installation

Python3 must be already installed

```shell
git clone https://github.com/artemgrishko/restaurant-kitchen-service.git
cd restaurant-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserever # starts Django Server
```

## Features

* Authentication functionality for Cook/User
* Managing dishes, cooks & dishes types directly from website interface
* Powerful admin panel for advanced managing
