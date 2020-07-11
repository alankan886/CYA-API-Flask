# CYA
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a) ![Flask](https://img.shields.io/badge/Flask-1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-RESTful](https://img.shields.io/badge/Flask--RESTful-0.3.8-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-2.5.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-JWT-Extended](https://img.shields.io/badge/Flask--JWT--Extended-3.24.1-blue.svg?longCache=true&logo=json-web-tokens&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)![Flask-Marshmallow](https://img.shields.io/badge/Flask--Marshmallow-0.12.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.3.2-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a) ![Live](https://img.shields.io/badge/API-Live%20on%20Heroku-green.svg?style=flat-square&logo=heroku&colorA=4c566a&colorB=a3be8c) ![Cloud Database](https://img.shields.io/badge/Database-Live%20on%20AWS%20RDS-green.svg?style=flat-square&logo=amazon-aws&colorA=4c566a&colorB=a3be8c)
<br>[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/alankan2004.svg?style=social&label=Follow%20%40alankan2004)](https://twitter.com/alankan2004)

A RESTful API built in Flask for spaced repetition studying.

  

## Table of Contents

 - [Demo](#demo)
 - [Motivation](#motivation)
 - [Features](#features)
	 - Endpoints
		 - [User](#user)
		 - [Board](#board)
		 - [Card](#card)
- [Quick Start](#quickstart)
- [Technologies Used](#techused)
	 - RESTful API
	 - Testing
	 - Cloud 
	 - Env/Config
- [Project Structure](#pjstruct)
- [Database Structure](#dbstruct)
- [To-do](#todo)

  
<a name="demo"/> </br>
## Demo

Deployed at [https://cya-api.herokuapp.com/](https://cya-api.herokuapp.com/) (There is no UI that corresponds to the API at the moment.)

 1. GIF Demo
 2. Video Demo

  
<a name="motivation"/> </br>
## Motivation
<tab> The reason behind making this API is for my own studying. I always been interested in self-improvement, time management and effective learning, so I been practicing spaced repetition more and more to help myself learn Data Structure and Algorithms.

And I thought it would be a great opportunity for me to learn building a fullstack web application and dig more into the science of spaced repetition, so I started off with building the backend first, which is the REST API you see now.

If you are curious of what spaced repetition is, check this out: [https://ncase.me/remember/](https://ncase.me/remember/)
  
<a name="features"/> </br>
## Features
To interact with the REST API, here are the endpoints categorized by resources.

### Endpoints
<a name="user"/> </br>
#### User


<a name="board"/> </br>
#### Board
<a name="card"/> </br>
#### Card

<a name="quickstart"/> </br>
## Quick Start

<a name="techused"/> </br>
## Technologies Used
### RESTful API

:clipboard:&nbsp;API <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask* <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-RESTful*

:clipboard:&nbsp;ORM (Object Relational Mapper) <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-SQLAlchemy*

:clipboard:&nbsp;Data Serialization <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-Marshmallow*

:clipboard:&nbsp;Database Migration <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-Migrate (alembic)*


:clipboard:&nbsp;Token Authentication <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-JWT-Extended*

:clipboard:&nbsp;Spaced Repetition Algorithm <br/> &nbsp;&nbsp;&nbsp;:pushpin: SuperMemo2 (My own package!)

### Testing
:clipboard:&nbsp;Unit & Integration Testing <br/> &nbsp;&nbsp;&nbsp;:pushpin: Unittest (Built-in Python Library) <br/> &nbsp;&nbsp;&nbsp;:pushpin: Nose2

### Cloud

 :clipboard:&nbsp;Service Hosting <br/> &nbsp;&nbsp;&nbsp;:pushpin: Heroku
 
:clipboard:&nbsp;Database <br/> &nbsp;&nbsp;&nbsp;:pushpin: AWS RDS

### Env/Config
:clipboard:&nbsp;Python-Dotenv <br/> &nbsp;&nbsp;&nbsp;:pushpin: *For easier local configurations using dotenv file.*

<a name="pjstruct"/> </br>
## Project Structure
```bash
.
├── Procfile
├── README.md
├── app
│   ├── __init__.py
│   ├── blacklist.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   ├── jwt
│   │   │   ├── __init__.py
│   │   │   └── loaders.py
│   │   └── main
│   │       ├── __init__.py
│   │       ├── db.py
│   │       ├── errors.py
│   │       └── routes.py
│   ├── extensions
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── jwt.py
│   │   ├── ma.py
│   │   └── migrate.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── board.py
│   │   ├── card.py
│   │   ├── card_sm_info.py
│   │   └── user.py
│   ├── resources
│   │   ├── __init__.py
│   │   ├── board.py
│   │   ├── card.py
│   │   ├── card_sm_info.py
│   │   └── user.py
│   └── schemas
│       ├── __init__.py
│       ├── board.py
│       ├── card.py
│       ├── card_sm_info.py
│       └── user.py
├── config.py
├── cya.py
├── migrations
│   └── alembic.ini
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── integration
│   │   ├── __init__.py
│   │   └── test_card_sm_info_resource.py
│   └── unit
│       ├── __init__.py
│       └── test_basics.py
└── venv
```

<a name="dbstruct"/> </br>
## Database Structure

![](/images/cyaDB.jpg)


<a name="todo"/> </br>
## To-do

- [ ] I'm planning on adding a frontend to this project, creating a SPA that interacts with the API.
	 - Technologies I'm planning to use are React, TypeScript and either Redux or Hooks.
- [ ] Implement the spaced repetition algorithm for calculating the next review date.
- [ ] Learning Redis and implementing it for JWT tokens.
- [ ] Password hashing before storing to database.
- [ ] Add created_at column in all the database tables.

