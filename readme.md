# Movies RESTful API

https://movies-api-flask.herokuapp.com/

Simple web service for parsing top movies from IMDb and represent them like RESTful API. 
Developed using Python, Flask and Sanic frameworks and PostgreSQL database. Deployed on Heroku.
Supports GET, POST, PUT, PATCH and DELETE methods for Movies and Actors entities. 
Some of them require tokens, thus user registration, authentication and authorization are also provided. 
Swagger is also added to the project. 
The DB can be populated either by using pre-defined set of values or by sing parsing top movies from IMBd. 
The parser can work in sequential, multithreading or multiprocessing modes.
Unittests realised using Pytest and Coverage.

- Language - Python
- Frameworks - Flask and minority Sanic
- Databases - SQLite and PostgreSQL
- ORM - SQLAlchemy
- Authentication - JWT
- Validation - Marshmallow
- API UI - Swagger
- Parsing - Beautiful Soup 4 and Requests
- WSGI - Gunicorn
- Containerization - Docker
- Deployment - Heroku
- Testing - Pytest and Coverage.

