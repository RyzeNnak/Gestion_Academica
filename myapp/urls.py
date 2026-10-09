from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),         # /myapp/ → login
    path('dashboard/', views.index, name='index'),    # /myapp/dashboard/ → plataforma
    path('index.html', RedirectView.as_view(url='/myapp/dashboard/')),  # redirección vieja
]