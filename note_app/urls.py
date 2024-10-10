from django.contrib import admin
from django.urls import path, include
from notes import views  # Importiere die Views aus der notes-App

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Index-Route
    path('notes/', include('notes.urls')),
]