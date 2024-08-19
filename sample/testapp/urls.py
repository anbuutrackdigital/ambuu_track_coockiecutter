from django.urls import path
from sample.testapp.views import dashboard

app_name = "testapp"

urlpatterns = [
    path("", view=dashboard, name="dashboard"),
]
