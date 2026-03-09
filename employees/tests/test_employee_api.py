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


@pytest.mark.django_db
def test_retrieve_employee():
    employee = Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )

    client = APIClient()
    url = reverse("employee-detail", args=[employee.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == employee.id
    assert response.data["full_name"] == "John Doe"
    assert response.data["job_title"] == "Software Engineer"
    assert response.data["country"] == "India"


@pytest.mark.django_db
def test_update_employee():
    employee = Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )

    client = APIClient()

    url = reverse("employee-detail", args=[employee.id])

    updated_data = {
        "full_name": "John Doe",
        "job_title": "Senior Software Engineer",
        "country": "India",
        "salary": 120000,
    }

    response = client.put(url, updated_data, format="json")

    assert response.status_code == 200
    assert response.data["job_title"] == "Senior Software Engineer"
    assert response.data["salary"] == "120000.00"


@pytest.mark.django_db
def test_delete_employee():
    employee = Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )

    client = APIClient()
    url = reverse("employee-detail", args=[employee.id])

    response = client.delete(url)

    assert response.status_code == 204
    assert Employee.objects.filter(id=employee.id).count() == 0


@pytest.mark.django_db
def test_salary_calculation_india():
    employee = Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )

    client = APIClient()

    url = reverse("employee-salary", args=[employee.id])

    response = client.get(url)

    assert response.status_code == 200
    assert response.data["gross_salary"] == 100000
    assert response.data["deduction"] == 10000
    assert response.data["net_salary"] == 90000


@pytest.mark.django_db
def test_salary_calculation_united_states():
    employee = Employee.objects.create(
        full_name="Jane Smith",
        job_title="QA Engineer",
        country="United States",
        salary=100000,
    )

    client = APIClient()
    url = reverse("employee-salary", args=[employee.id])

    response = client.get(url)

    assert response.status_code == 200
    assert response.data["gross_salary"] == 100000
    assert response.data["deduction"] == 12000
    assert response.data["net_salary"] == 88000