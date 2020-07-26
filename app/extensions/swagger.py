from flasgger import Swagger

template = {
    "info": {
        "title": "CYA API",
        "description": "A RESTful API for spaced repetition learning.",
        "contact": {
            "name": "Developer",
            "url": "https://github.com/alankan2004"
        },
        "license": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT"
        },
        "version": "0.1.0"
    },
    "components": {
        "schemas": {
            "User": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int"
                    },
                    "username": {
                        "type": "string",
                        "required": "true"
                    },
                    "password": {
                        "type": "string",
                        "required": "true"
                    }
                }
            },
            "Board": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int"
                    },
                    "user_id": {
                        "type": "int"
                    },
                    "name": {
                        "type": "string",
                        "required": "true"
                    }
                }
            },
            "Card": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int"
                    },
                    "name": {
                        "type": "string",
                        "required": "true"
                    },
                    "tag": {
                        "type": "string"
                    },
                    "quality": {
                        "type": "int",
                        "required": "true"
                    },
                    "last_review": {
                        "type": "date"
                    },
                    "next_review": {
                        "type": "date"
                    },
                    "board_id": {
                        "type": "int",
                    }
                }
            },
            "Card-SM-Info": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int"
                    },
                    "quality": {
                        "type": "int",
                        "required": "true"
                    },
                    "last_review": {
                        "type": "date"
                    },
                    "next_review": {
                        "type": "date"
                    },
                    "board_id": {
                        "type": "int"
                    },
                    "new_interval": {
                        "type": "int"
                    },
                    "new_repetitions": {
                        "type": "int"
                    },
                    "new_easiness": {
                        "type": "float"
                    }
                }
            }
        },
        "securitySchemes": {
           "bearerAuth": {    
               "in": "header",       
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
           }
        },
        "responses": {
            "UnauthorizedError": {
                "description": "Access token is missing or invalid"
            }
        }
    }
}

swagger = Swagger(template=template)
