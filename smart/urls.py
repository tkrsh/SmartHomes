from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='portal'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutpage, name='logout'),
    path('out/',views.jsondump, name='api'),
]
