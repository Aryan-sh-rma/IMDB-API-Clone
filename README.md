
# IMDB API Clone

## A brief description of project :
- A REST API has been used to make a backend of Movie review platform.
- User can login and see list of movies and review them.
- The rating of the movie will be displayed based on different user ratings and reviews.

## Permissions to admin : 
- Add Streaming Platform detail
- Add movies on Patforms
- Edit  Streaming Platform and movie details
## Permissions to User :
- Only see Streaming Platform detail
- Only see movie details on Patforms
- Add Edit Or delete reviews
- Give ratings to movie



## Installation

Install my-project using these commands
```bash
git clone https://github.com/Aryan-sh-rma/IMDB-API-Clone.git

cd IMDB-API-Clone

pip install virtualenv

virtualenv [env name]

env\Scripts\activate


```
After Cloning-Install below version in terminal and 'New Version will face version conflict error' 
``` bash
asgiref==3.7.2
Django==5.0
django-filter==23.5
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
PyJWT==2.8.0
pytz==2023.3.post1
sqlparse==0.4.4
tzdata==2023.3


```

## For Admin Login
You can use any username or password
```bash
python manage.py createsuperuser
Username : admin
Password : admin
```


## Appendix

Use POSTMAN for testing these APIs.


