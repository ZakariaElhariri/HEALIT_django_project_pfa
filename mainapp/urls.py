# mainapp/urls.py

from django.urls import path
from . import views
#username:zak
#password:zak
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('reserve/', views.reserve, name='reserve'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('salma/', views.salma, name='salma'),
    path('admin_connection/', views.admin_connection, name='admin_connection'),
]

