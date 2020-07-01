# CYA
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a) ![Flask](https://img.shields.io/badge/Flask-1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-RESTful](https://img.shields.io/badge/Flask--RESTful-0.3.8-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-2.5.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-JWT-Extended](https://img.shields.io/badge/Flask--JWT--Extended-3.24.1-blue.svg?longCache=true&logo=json-web-tokens&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)![Flask-Marshmallow](https://img.shields.io/badge/Flask--Marshmallow-0.12.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.3.2-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a) ![Live](https://img.shields.io/badge/API-Live%20on%20Heroku-green.svg?style=flat-square&logo=heroku&colorA=4c566a&colorB=a3be8c) ![Cloud Database](https://img.shields.io/badge/Database-Live%20on%20AWS%20RDS-green.svg?style=flat-square&logo=amazon-aws&colorA=4c566a&colorB=a3be8c)
<br>[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/alankan2004.svg?style=social&label=Follow%20%40alankan2004)](https://twitter.com/alankan2004)

A RESTful API built in Flask for spaced repetition studying.

  

## Table of Contents

 - Demo
 - Motivation
 - Quick Start
	 - Endpoints
		 - User
		 - Board
		 - Card
- Technologies Used
	 - RESTful API
	 - Cloud 
- Project Structure
- Database Structure
- To-do

  

## Demo

Deployed at [https://cya-api.herokuapp.com/](https://cya-api.herokuapp.com/) (There is no UI that corresponds to the API at the moment.)

 1. GIF Demo
 2. Video Demo

  

## Motivation
The reason behind making this API is for my own studying. I always been interested in self-improvement, time management and effective learning, so I been practicing spaced repetition more and more to help myself learn Data Structure and Algorithms. And I thought it would be a great opportunity for me to learn building a fullstack web application and dig more into the science of spaced repetition, so I started off with building the backend first, which is the REST API you see now.

If you are curious of what spaced repetition is, check this out: [https://ncase.me/remember/](https://ncase.me/remember/)
  

## Quick Start
To interact with the REST API, here are the endpoints categorized by resources.

### Endpoints
#### User
#### Board
#### Card

## Technologies Used
### RESTful API
 - #### Flask
	 - *Flask-RESTful*
	 - *Flask-Migrate (alembic)*
 - #### SQLAlchemy
	 - *Flask-SQLAlchemy*
	 - For ORM (Object Relational Mapper).
- #### Marshmallow
	- *Flask-Marshmallow*
- #### JWT (Json Web Token)
	- *Flask-JWT-Extended*
- #### Unittest
	- For unit testing.
- #### Python-Dotenv
	- For easier local configurations using .env file.

### Cloud

 - #### Hosting :arrow_right: Heroku
 - #### Database :arrow_right: AWS RDS

## To-do

 1. I'm planning on adding a frontend to this project, creating a SPA that interacts with the API.
	 - Technologies I'm planning to use are React, TypeScript and either Redux or Hooks.
 2. I really want to add a feature such that the API automatically calculates the next review date base on the spaced repetition rules.
 3. Learning Redis and implementing it for JWT tokens.
 4. Password hashing before storing to database.

