from django.contrib import admin
from django.urls import path, include  # include is needed
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('/todo/login/')),

    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls')),  # correct usage
]
