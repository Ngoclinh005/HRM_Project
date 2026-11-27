
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard_home, name="dashboard_home"),
    path("employees/", views.employees_view, name="employees"),
    path("logout/", views.logout_view, name="logout"),
]

