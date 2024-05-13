from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("profile/", views.ProfileView, name="profile"),
    path("add-slot/", views.AddSlotView, name="add_slot"),
    path("reserve/", views.ReserveView, name="reserve"),
]
