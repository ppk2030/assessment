from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, SalaryMetricsByCountryView, SalaryMetricsByJobTitleView
from django.urls import path

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = router.urls

urlpatterns += [
    path(
        "salary-metrics/country/<str:country>/",
        SalaryMetricsByCountryView.as_view(),
        name="salary-metrics-country",
    ),
]

urlpatterns += [
    path(
        "salary-metrics/job-title/<str:job_title>/",
        SalaryMetricsByJobTitleView.as_view(),
        name="salary-metrics-job-title",
    ),
]