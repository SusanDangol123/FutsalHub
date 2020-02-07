from django.urls import path
from .import views


urlpatterns = [
    path("",views.home, name=" home "),
    path("home",views.home, name=" home "),


    path("balaju",views.balaju, name=" home "),
    path("thamel",views.thamel, name=" home "),
    path("dillizabazar",views.dillizabazar, name=" home "),

    path("thimi", views.thimi, name=" home "),
    path("suryabinayak", views.suryabinayak, name=" home "),
    path("changunarayan", views.changunarayan, name=" home "),

    path("patan", views.patan, name=" home "),
    path("kumaripati", views.kumaripati, name=" home "),
    path("jawalakhel", views.jawalakhel, name=" home "),


    path("login",views.login, name=" home "),
    path("signup",views.signup, name=" home "),
    path("training",views.training,name="training"),


    path("adminlogin", views.adminLogin, name="login page"),
    path("entry", views.entry, name="login page"),

    path("dashboard", views.dashboard, name="dashboard page"),

    path("entryCustomer", views.entryCustomer, name="login page"),
    path("showCustomer", views.showCustomer, name="showCustomer page"),

    path("create", views.create, name="Create page"),
    path("show", views.show, name="show page"),
    path("edit/<int:id>", views.edit, name="edit page"),
    path("update/<int:id>", views.update, name="update page"),
    path("delete/<int:id>", views.delete, name="delete page"),
]
