
from rest_framework import status, viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from decimal import Decimal
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=["get"])
    def salary(self, request, pk=None):
        employee = self.get_object()
        gross_salary = employee.salary

        if employee.country == "India":
            deduction_rate = Decimal("0.10")
        elif employee.country == "United States":
            deduction_rate = Decimal("0.12")
        else:
            deduction_rate = Decimal("0.00")

        deduction = gross_salary * deduction_rate
        net_salary = gross_salary - deduction

        return Response(
            {
                "employee_id": employee.id,
                "gross_salary": float(gross_salary),
                "deduction": float(deduction),
                "net_salary": float(net_salary),
            },
            status=status.HTTP_200_OK,
        )
