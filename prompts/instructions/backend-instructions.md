# Backend Instructions

Use this guide for backend work in the project.

It uses FastAPI, SQLAlchemy, Pydantic, and RESTful API design principles.

Write the complete code for every step. Do not get lazy. Write everything that is needed.

Your goal is to completely finish whatever the user asks for.

## Steps

- all endpoints should be defined in `/api/api.py`
- database utilities should be defined in `/api/database.py`
- new models should be defined in `/api/db/models/` like @example-model.py
- new schemas go in a new schema file in `/api/db/schemas/` like @example-schema.py
- new data operations should be defined in `/api/db/crud.py`
- you may also be asked to implement frontend features, so make sure the above is complete before building out those frontend features

## Requirements

- data should be delivered in JSON format
- data validation should be done using Pydantic
- database operations should be done using SQLAlchemy
- the RESTful API design principles should be followed
