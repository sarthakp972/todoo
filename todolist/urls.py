from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('todos/',views.todos,name='todos'),
    path('logout/', views.user_logout, name='logout'),
]
