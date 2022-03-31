from django.urls import path
from .import views
urlpatterns = [
    path('',views.store),
    path('create/',views.addBook),
    path('outstoks/',views.outOfStoks),
    path('edit/<int:bid>/',views.editBook),
    path('listout/<int:bid>/',views.listOut),
    path('deletebook/<int:bid>/',views.deleteBook),

]