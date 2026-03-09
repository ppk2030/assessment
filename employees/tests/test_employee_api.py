import pytest
from rest_framework.test import APIClient

from employees.models import Employee


@pytest.mark.django_db
def test_create_employee():
    client = APIClient()

    data = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000,
    }

    response = client.post("/employees/", data, format="json")

    assert response.status_code == 201
    assert response.data["full_name"] == "John Doe"


@pytest.mark.django_db
def test_list_employees():
    Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )
    Employee.objects.create(
        full_name="Jane Smith",
        job_title="QA Engineer",
        country="United States",
        salary=120000,
    )

    client = APIClient()
    response = client.get("/employees/")

    assert response.status_code == 200
    assert len(response.data) == 2