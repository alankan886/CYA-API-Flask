# CYA
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![made-with-flask](https://img.shields.io/badge/Made%20with-Flask-1f425f.svg)](https://www.python.org/) [![Website cv.lbesson.qc.to](https://img.shields.io/website-up-up-green-red/http/cv.lbesson.qc.to.svg)](http://cv.lbesson.qc.to/)

  

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
 - To-do

  

## Demo

Deployed at [https://cya-api.herokuapp.com/](https://cya-api.herokuapp.com/) (There is no UI that corresponds to the API at the moment.)

 1. GIF Demo
 2. Video Demo

  

## Motivation
The reason behind making this API is for my own studying. I always been interested in self-improvement, time management and effective learning, so I been practicing spaced repetition more and more to help myself learn Data Structure and Algorithms. And I thought it would be a great opportunity for me to learn building a fullstack web application and dig more into the science of spaced repetition, so I started off with building the backend first, which is the REST API you see now.

If you are curious of what spaced repetition is, check this out: [https://ncase.me/remember/](https://ncase.me/remember/)
  

## Quick Start

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
- #### JWT
	- *Flask-JWT-Extended*
- #### Unittest
	- For unit testing.
- #### Python-Dotenv
	- For easier local configurations using .env file.

### Cloud

 - #### Hosting :arrow_right: Heroku
 - #### Database :arrow_right: AWS RDS

#### Hosting
## To-do

 1. I'm planning on adding a frontend to this project, creating a SPA that interacts with the API.
	 - Technologies I'm planning to use are React, TypeScript and either Redux or Hooks.
 2. I really want to add a feature such that the API automatically calculates the next review date base on the spaced repetition rules.
 3. Learning Redis and implementing it for JWT tokens.
