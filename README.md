# CYA
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a) ![Flask](https://img.shields.io/badge/Flask-1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-RESTful](https://img.shields.io/badge/Flask--RESTful-0.3.8-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-2.5.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-JWT-Extended](https://img.shields.io/badge/Flask--JWT--Extended-3.24.1-blue.svg?longCache=true&logo=json-web-tokens&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)![Flask-Marshmallow](https://img.shields.io/badge/Flask--Marshmallow-0.12.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.3.2-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a) ![Status](https://img.shields.io/badge/Development%20Status-Alpha-critical.svg?style=flat-square&logo=atom&colorA=4c566a&colorB=critical) ![Coverage](https://img.shields.io/badge/Coverage-60%25-light--green.svg?style=flat-square&colorA=4c566a&colorB=90BCA8)  ![Live](https://img.shields.io/badge/API-Live%20on%20Heroku-green.svg?style=flat-square&logo=heroku&colorA=4c566a&colorB=a3be8c) ![Cloud Database](https://img.shields.io/badge/Database-Live%20on%20AWS%20RDS-green.svg?style=flat-square&logo=amazon-aws&colorA=4c566a&colorB=a3be8c) 
<br>[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/alankan2004.svg?style=social&label=Follow%20%40alankan2004)](https://twitter.com/alankan2004)

A RESTful API built in Flask for spaced repetition studying.

  

## Table of Contents

 - [Demo](#demo)
 - [Motivation](#motivation)
 - [Features](#features)
 - [API Reference Index](#api-ref-index)
	 1. [User](#user)
		 - [POST /register](#post-register)
		 - [POST /login](#post-login)
		 - [POST /logout](#post-logout)
		 - [POST /refresh](#post-refresh)
	 2. [Board](#board) 
		 - [GET /boards](#get-boards)
		 - [GET /<board_name>](#get-board_name)
		 - [POST /<board_name>](#post-board_name)
		 - [PUT /<board_name>](#put-board_name)
		 - [DELETE /<board_name>](#delete-board_name)
	 3. [Card](#card)
		 - [GET /cards](#get-cards)
		 - [GET <board_name>/cards](#get-board_name-cards)
		 - [DELETE <board_name>/cards](#delete-board_name-cards)
		 - [GET <board_name>/<card_name>](#get-board_name-card_name)
		 - [POST <board_name>/<card_name>](#post-board_name-card_name)
		 - [PUT <board_name>/<card_name>](#put-board_name-card_name)
		 - [DELETE <board_name>/<card_name>](#delete-board_name-card_name)
	 4. [Card-SM-Info](#card-sm-info)
		 - [GET <board_name>/<card_name>/all-sm2-info](#get-board_name-card_name-all_sm2_info)
		 - [POST <board_name>/<card_name>/sm2-info](#post-board_name-card_name-sm2_info)
		 - [PUT <board_name>/<card_name>/sm2-info/\<id>](#put-board_name-card_name-sm2_info-id)
		 - [DELETE <board_name>/<card_name>/sm2-info/\<id>](#delete-board_name-card_name-sm2_info-id)
- [Quick Start](#quickstart)
- [Technologies Used](#techused)
	 1. [RESTful API](#restful-api)
	 2. [Testing](#testing)
		 - Coverage Details
	 3. [Cloud](#cloud) 
	 4. [Env/Config](#env)
- [Project Structure](#pjstruct)
- [Database Structure](#dbstruct)

  
<a name="demo"/> </br>
## Demo

OpenAPI/Swagger UI document deployed at [https://cya-api.herokuapp.com/apidocs/](https://cya-api.herokuapp.com/apidocs/) (There is no UI that corresponds to the API at the moment.)

![](/images/OpenAPI.png)

<a name="motivation"/> </br>
## Motivation
<tab> The reason behind making this API is for my own studying. I always been interested in self-improvement, time management and effective learning, so I been practicing spaced repetition more and more to help myself learn Data Structure and Algorithms.

And I thought it would be a great opportunity for me to learn building a fullstack web application and dig more into the science of spaced repetition, so I started off with building the backend first, which is the REST API you see now.

If you are curious of what spaced repetition is, check this out: [https://ncase.me/remember/](https://ncase.me/remember/)
  
<a name="features"/> </br>
## Features

 - API follows the RESTful design.
 - Allows multiple users to access the API.
 - API calculates the next review date for whatever you are learning based on the spaced repetition learning algorithm SuperMemo-2.
 - OpenAPI/Swagger UI supported for simpler access for developers.

<a name="api-ref-index"/> </br>
## API Reference Index 

<a name="user"/> </br>
### User
| Field | Description |
|--|--|
| **id** | The user's id |
| username | The user's unique username |

<a name="post-register"/> </br>
### POST /register
#### Resource URL
`https://cya-api.herokuapp.com/register`

#### Resource Information
|||
|--|--|
| Response format | JSON |
| Requires authentication? | No |

<a name="post-login"/> </br>
### POST /login
#### Resource URL
`https://cya-api.herokuapp.com/login`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | No |

<a name="post-logout"/> </br>
### POST /logout
#### Resource URL
`https://cya-api.herokuapp.com/logout`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="post-refresh"/> </br>
### POST /refresh
#### Resource URL
`https://cya-api.herokuapp.com/refresh`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

---
<a name="board"/> </br>
### Board
| Field | Description |
|--|--|
| **id** | The board's id. |
| name | The board's unique name. |
| user_id | The user id of the user that owns this board. |

<a name="get-boards"/> </br>
### GET /boards
#### Resource URL
`https://cya-api.herokuapp.com/<username>/boards`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="get-board_name"/> </br>
### GET /<board_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="post-board_name"/> </br>
### POST /<board_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="put-board_name"/> </br>
### PUT /<board_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="delete-board_name"/> </br>
### DELETE /<board_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

---
<a name="card"/> </br>
### Card
| Field | Description |
|--|--|
| **id** | The card's id. |
| name | The card's unique name. |
| tag | The category tag that attaches to the card |
| quality | The quality of the review. Check [here](https://github.com/alankan2004/SuperMemo2/blob/master/README.md#qism2) for more detail description. |
| last_review | The date of the last time this card is reviewed. |
| next_review | The date of the next time this card should be reviewed. |
| board_id | The board id of the board that card belongs to. |

<a name="get-cards"/> </br>
### GET /cards
**Note:** This endpoint will most likely be removed and change the today resource to a query parameter instead.

#### Resource URL
`https://cya-api.herokuapp.com/<username>/cards/today`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |
<br/>

|Parameters|type|value|required|
|--|--|--|--|
| today | boolean | true/false | No

<a name="get-board_name-cards"/> </br>
### GET /<board_name>/cards
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/cards`

<a name="delete-board_name-cards"/> </br>
### DELETE /<board_name>/cards
**Note:** The API is in Alpha, so please use this with caution, once it's deleted it's gone. There will be warnings in the future.
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/cards`

|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="get-board_name-card_name"/> </br>
### GET /<board_name>/<card_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="post-board_name-card_name"/> </br>
### POST /<board_name>/<card_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="put-board_name-card_name"/> </br>
### PUT /<board_name>/<card_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="delete-board_name-card_name"/> </br>
### DELETE /<board_name>/<card_name>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

---
<a name="card-sm-info"/> </br>
### Card-SM-Info
This is for the card's SuperMemo2 information.
| Field | Description |
|--|--|
| **id** | The card's id. |
| quality | The quality of the review. Check [here](https://github.com/alankan2004/SuperMemo2/blob/master/README.md#qism2) for more detail description. |
| new_interval | The card's new calculated interval value using the SuperMemo-2 algorithm.|
| new_repetitions | The card's new calculated repetitions value using the SuperMemo-2 algorithm. |
| new_easiness | The card's new calculated easiness value using the SuperMemo-2 algorithm. |
| last_review | The date of the last time this card is reviewed. |
| next_review | The date of the next time this card should be reviewed. |
| board_id | The board id of the board that card belongs to. |

<a name="get-board_name-card_name-all_sm2_info"/> </br>
### GET /<board_name>/<card_name>/all-sm2-info
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>/all-sm2-info`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="post-board_name-card_name-sm2_info"/> </br>
###  POST /<board_name>/<card_name>/sm2-info
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>/sm2-info`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="put-board_name-card_name-sm2_info-id"/> </br>
### PUT /<board_name>/<card_name>/sm2-info/\<id>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>/sm2-info/<id>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="delete-board_name-card_name-sm2_info-id"/> </br>
### DELETE /<board_name>/<card_name>/sm2-info/\<id>
#### Resource URL
`https://cya-api.herokuapp.com/<username>/<board_name>/<card_name>/sm2-info/<id>`
|||
|--|--|
| Response format | JSON |
| Requires authentication? | Yes |

<a name="quickstart"/> </br>
## Quick Start
Coming soon...
<a name="techused"/> </br>
## Technologies Used
<a name="restful-api"/> </br>
### RESTful API

:clipboard:&nbsp;**API** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask* <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-RESTful*

:clipboard:&nbsp;**ORM (Object Relational Mapper)** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-SQLAlchemy*

:clipboard:&nbsp;**Data Serialization** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-Marshmallow*

:clipboard:&nbsp;**Database Migration** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-Migrate (alembic)*


:clipboard:&nbsp;**Token Authentication** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *Flask-JWT-Extended*

:clipboard:&nbsp;**Spaced Repetition Algorithm** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *SuperMemo2 (My own package!)*

---
<a name="testing"/> </br>
### Testing
:clipboard:&nbsp;**Unit & Functional Testing** <br/> &nbsp;&nbsp;&nbsp;:pushpin: Pytest (Built-in Python Library) <br/> &nbsp;&nbsp;&nbsp;:pushpin: Pytest-Cov

#### Coverage Details
![](/images/cya-api-coverage.png)

---
<a name="cloud"/> </br>
### Cloud

 :clipboard:&nbsp;**Service Hosting** <br/> &nbsp;&nbsp;&nbsp;:pushpin: Heroku
 
:clipboard:&nbsp;**Database** <br/> &nbsp;&nbsp;&nbsp;:pushpin: AWS RDS

---
<a name="env"/> </br>
### Env/Config
:clipboard:&nbsp;**Python-Dotenv** <br/> &nbsp;&nbsp;&nbsp;:pushpin: *For easier local configurations using dotenv file.*

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

![](/images/cyaDB.jpg)

