from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('userlogin/', views.user_login, name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.user_logout, name='user_logout'),
    path('changepass/', views.change_password, name='change_password'),
]
