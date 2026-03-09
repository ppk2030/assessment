import pytest
from rest_framework.test import APIClient
from django.urls import reverse

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

    url = reverse("employee-list")
    response = client.post(url, data, format="json")

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

    url = reverse("employee-list")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2