# crud_exercise


## Screenshots

| Column                          |                    
|---------------------------------|
| ![Home](screenshots/01.png)     |                              
|                                 |                              

## About

Putting in practice concepts learned about jQuery, Bootstrap, javaScript, Python and Django.

## Installation

- Create a virtual environment with python 3.6. In my case I used conda for that.
```shell
conda create -n crudEnv python=3.6
```
- Activate the virtual environment you have just created:
```shell
conda activate crudEnv
```
- Clone the repository:
```shell
git clone https://github.com/albertosdneto/django_crud.git
```
- Go to the crudProject folder and install the requirements:
```shell
cd django_crud

cd crudProject

pip install -r requirements.txt
```
- Setup environment variables or setup these values inside ```settings.py```:
``` python
SECRET_KEY = "#####################"

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
