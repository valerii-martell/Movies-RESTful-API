# Movies RESTful API

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/638324c7268a44e6915c6f9f313300d3)](https://www.codacy.com/gh/valerii-martell/Movies-RESTful-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=valerii-martell/Movies-RESTful-API&amp;utm_campaign=Badge_Grade)
[![Flake8](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/lint.yml/badge.svg)](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/lint.yml)
[![Pytest](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/test.yml/badge.svg)](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/test.yml)
[![CodeQL](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/codeql.yml/badge.svg)](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/codeql.yml)
[![Docker](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/docker.yml/badge.svg)](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/docker.yml)
[![Deploy](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/deploy.yml/badge.svg)](https://github.com/valerii-martell/Movies-RESTful-API/actions/workflows/deploy.yml)



https://movies-api-flask.herokuapp.com/

A simple web service for parsing top movies from IMDb and represent them like RESTful API. 
Developed using Python language, Flask and Sanic frameworks and PostgreSQL database. Deployed on Heroku.
Supports GET, POST, PUT, PATCH and DELETE methods for Movies and Actors entities. 
Some of them require tokens, thus user registration, authentication and authorization are also provided. 
Swagger is also added to the project. 
The DB can be populated either by using pre-defined set of values or by sing parsing top movies from IMBd. 
The parser can work in sequential, multithreading or multiprocessing modes.
Unittests realised using Pytest and Coverage.

**Technology stack:**
- Language - Python
- Frameworks - Flask and minority Sanic
- Databases - SQLite and PostgreSQL
- ORM - SQLAlchemy
- Authentication - JWT
- Validation - Marshmallow
- Frontend: Jinja2 and Bootstrap 4
- API UI - Swagger
- Parsing - Beautiful Soup 4 and Requests
- WSGI - Gunicorn
- Testing - Pytest and Coverage.
- Linter - Flake8
- Containerization - Docker
- Deployment - Heroku
- CI/CD - GitHub Actions 

**DB structure:** https://drawsql.app/kpi-6/diagrams/movies-api-db
![drawSQL-export-2022-07-10_06_46](https://user-images.githubusercontent.com/19497575/178131742-7ba1e30c-7a54-4b27-97d3-4d049ad33dc4.png)



