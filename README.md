Employee Salary API

This project implements a REST API for managing employees and computing salary deductions and salary metrics. The application is built using Django and Django REST Framework, with SQLite used as the database.

The solution was developed following a Test-Driven Development (TDD) workflow where tests were written first and the implementation was added incrementally to satisfy those tests.

Tech Stack

Python
Django
Django REST Framework
SQLite
Pytest
Black / isort / flake8

Swagger API documentation is available at:

/api/docs/

Setup Instructions
1. Clone the repository
git clone <repository-url>
cd assessment
2. Create a virtual environment
python -m venv venv

Activate the environment.

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Apply database migrations
python manage.py migrate
5. Run the application
python manage.py runserver

The API will run at:

http://127.0.0.1:8000
Running Tests

Run all tests using:

pytest
Linting and Formatting

Format the code:

black .
isort .

Run lint checks:

flake8
API Endpoints
Employee CRUD

POST /employees/
Create an employee.

GET /employees/
List all employees.

GET /employees/{id}/
Retrieve a specific employee.

PUT /employees/{id}/
Update employee information.

DELETE /employees/{id}/
Delete an employee.

Salary Calculation

GET /employees/{id}/salary/

This endpoint calculates salary deductions and the resulting net salary based on the employee's country.

Deduction rules:

India → 10% deduction
United States → 12% deduction
All other countries → no deduction

Example response

{
  "employee_id": 1,
  "gross_salary": 100000,
  "deduction": 10000,
  "net_salary": 90000
}
Salary Metrics by Country

GET /salary-metrics/country/{country}/

Returns minimum, maximum, and average salary for employees in the given country.

Example response

{
  "country": "India",
  "min_salary": "100000.00",
  "max_salary": "120000.00",
  "avg_salary": "110000.00"
}
Salary Metrics by Job Title

GET /salary-metrics/job-title/{job_title}/

Returns the average salary for employees with the specified job title.

Example response

{
  "job_title": "Software Engineer",
  "avg_salary": "110000.00"
}
Testing Approach (TDD)

The project was developed using Test-Driven Development.

Each feature followed the typical TDD cycle:

Write a failing test

Implement the minimal code required to pass the test

Refactor while keeping tests passing

Tests cover:

Employee CRUD functionality

Salary deduction calculations

Salary metrics endpoints

Validation logic such as preventing negative salaries

Design Decisions

Django REST Framework ViewSets

ModelViewSet was used for employee CRUD operations to reduce boilerplate and follow RESTful conventions.

Custom Endpoints

Custom endpoints such as salary calculation and salary metrics were implemented using dedicated views to keep business logic separate from CRUD functionality.

SQLite Database

SQLite was selected because it satisfies the assignment requirement and allows simple setup without additional infrastructure.

AI Usage

AI tools were used during development as a productivity aid to speed up routine tasks and explore implementation options. For example, they were helpful for:

brainstorming possible API structures and endpoint patterns

suggesting approaches for writing tests and validating edge cases

reviewing linting and formatting setup

helping draft and refine parts of the documentation

The AI suggestions were treated as starting points. The final code, design choices, and debugging were done manually, and all changes were reviewed carefully and validated through tests to ensure the solution behaves correctly and meets the assignment requirements.