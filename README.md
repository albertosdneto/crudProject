# Django CRUD


## Screenshots

| Column A                        | Column B                        | 
|---------------------------------|---------------------------------|
| ![Home](screenshots/01.png)     | ![Companies](screenshots/02.png)|                            
| ![NewComp](screenshots/03.png)  | ![InfoComp](screenshots/04.png) |

## About

Putting in practice concepts learned about jQuery, Bootstrap, javaScript, Python and Django.

## Installation

- Clone the repository and enter the folder crudProject:
```shell
git clone https://github.com/albertosdneto/crudProject.git
cd crudProject
```
- Create a virtual environment with python 3.6.
```shell
python3 -m venv venv
```
- Activate the virtual environment you have just created:
```shell
source venv/bin/activate
```
- Upgrade the virtual environment:
```shell
pip install --upgrade pip setuptools
```
- Install and configure PostgreSQL. On Ubuntu 18.04 do as follow:
```shell
sudo apt-get install postgresql postgresql-contrib
```
- Create passoword and database. For password I used '123456', but you may change it:
```shell
sudo -u postgres psql postgres
\password postgres
create database crudprojectdb;
\q
```
- Install gui for postgres:
```shell
sudo apt-get install pgadmin3
```
- For more information on how to setup PostgreSQL take a look at the links below:
  - <https://help.ubuntu.com/community/PostgreSQL>
  - <https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989>
  - <https://medium.com/@lucas_souto/integrando-django-com-postgresql-58b3520ddf6e>

- Install the requirements:
```shell
pip install -r requirements.txt
```

- Next to ```manage.py``` create the file ```.env``` with the content:
``` shell
DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DB_NAME=crudprojectdb
DB_USER=postgres
DB_PASS=123456
```

- Migrate database:
```shell
python manage.py makemigrations
python manage.py migrate
```
- Create Superuser:
```shell
python manage.py createsuperuser
```
- Run the project:
```shell
python manage.py runserver
```
- Go to the project url and verify if it is running. Enjoy.
