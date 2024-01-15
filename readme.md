

### TO ADD PROPERTIES,TENANT,UNITS CLICK ON THE HEADING ITSELF.....

This is an application build using Python Django and Django REST framework.

## Cloning the Repository and moving to the project level

```sh
git clone https://github.com/Itsmebewinbk/real_estate_management.git

cd moonhive_real_estate
```

## Installation and Setup

The application requires [Python](https://www.python.org/) v3.6+ to run.
Install the dependencies and requirements after creating a virtuale enviroment for the project.

```sh
python3 -m venv env
pip install -r requirements.txt
```

For Linux

```sh
source venv/bin/activate
mkdir logs   (create log directory)
echo 'SECRET_KEY="give an alpha numerical value*"' >> .env
```

Initializing the project

```sh
python manage.py migrate
```

Admin user creation (optional) for accessing the django admin

```sh
python manage.py createsuperuser
```

```sh
python manage.py loaddata countries.json states.json
```

## Running the project

```sh
python manage.py runserver
```

Once the serices are up, you can open the browser and navigate the below links

##### Home:

A basic index page

```sh
http://localhost:8000
```

##### Admin:

The Django admin UI

```sh
http://localhost:8000/api/admin/
```
### LIST OF ALL APIS:

```sh
http://localhost:8000/api/docs/
```
