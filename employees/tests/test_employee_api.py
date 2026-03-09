import pytest
from rest_framework.test import APIClient
from django.urls import reverse


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