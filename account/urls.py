from django.urls import path
from . import views

urlpatterns = [
    path('',views.Signup),
    path('login/',views.login),
    path('logout/',views.logout),
]