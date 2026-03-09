import pytest
from django.core.exceptions import ValidationError

from employees.models import Employee


@pytest.mark.django_db
def test_create_employee():
    employee = Employee.objects.create(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=100000,
    )

    assert employee.id is not None
    assert employee.full_name == "John Doe"
    assert employee.job_title == "Software Engineer"
    assert employee.country == "India"
    assert employee.salary == 100000


@pytest.mark.django_db
def test_employee_salary_cannot_be_negative():
    employee = Employee(
        full_name="John Doe",
        job_title="Software Engineer",
        country="India",
        salary=-1000,
    )

    with pytest.raises(ValidationError):
        employee.full_clean()
