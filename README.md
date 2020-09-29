# Perpay Interview Dashboard - Backend 
---
##### This backend is a django server that functions as a rest api for the frontend service (**[perpay-frontend](https://github.com/Sciguystfm/perpayFrontend)**)

&NewLine;
&NewLine;
##### - The hosted version of this application uses a PostgreSQL database
##### - The local version uses a lighterweight sqlite3 database
&NewLine;

##### The backend is minimally accessible on heroku:
## [https://perpay-backend.herokuapp.com/](https://perpay-backend.herokuapp.com/)

&NewLine;
&NewLine;
### Install Process (Docker) (Good luck)
---
##### 1. Clone a copy of the repo `https://github.com/Sciguystfm/perpayBackend.git`
##### 2. Modify the Dockerfile with the URL of your backend (`REACT_APP_BACKEND_URL`)
##### 3. Build the backend image `docker build -t backendlocal:1.0 .`
##### 4. Run the image as a container 
&NewLine;
```
docker run -d --name backend -e "PORT=8765" -e "DEBUG=1 -p 8007:8765 backendlocal:1.0"
```
##### 5. (Optionally) Run `docker ps` to find the container we just started and
##### 6. (Optionally) Using the following command, generate bulk testdata in our database
&NewLine;
```
docker exec -it CONTAINER_WE_LOOKED_UP python manage.py bulkcreate
```

#### If that worked,you should be good! The and the backend should be live on `localhost:8007/` 


&NewLine;
&NewLine;
### Install Process (*Not* Docker) (Something's gone horribly wrong)
---
##### 1. Clone a copy of the repo `https://github.com/Sciguystfm/perpayFrontend.git`
##### 2. Download and setup a virtualenv 
&NewLine;

```
python3 -m pip install virtualenv
python3 -m venv backendenv
source env/bin/activate
```
##### 3. Install requirements `pip -m install requirements.txt`
##### 4. Make and apply migrations `python manage.py makemigrations` && `python manage.py migrate`
##### 5. Run the setup function to create an initial company, admin user, and payment `python manage.py setup`
##### 6. (Optional) Generate bulk testdata with  `python manage.py bulkcreate`
##### 7. Finally, start the server with `python manage.py runserver`
&NewLine;

#### And at that point you should be good! The frontend should be live on localhost:8000/
(Don't forget to update the frontend with this url if you choose to do so!)
