# Project_4_Pragya
# Continuous Delivery of FastAPI Data Engineering API on AWS

The objective of this project is to create a microservice using FastAPI and deploy it on AWS. 
Building a CRUD application using FastAPI. 
CRUD/To-Do application
-Create
-Read 
-Update
-delete
 POST, PUT, and DELETE requests so we can modify our database. POST request is for adding data, a PUT request is typically for Updating data and a DELETE request is for, well, deleting data.

1. Scaffolding
A makefile, a requirements file, and the test files were created. They were all run by github actions as a measure of continuous integration. 

2. Fastapi 
    i. main. py - FastAPI APP
    ii. database.py - connection to sql
    iii. models.py- creating the table
    iv. dataschema- pydantic for data validation
