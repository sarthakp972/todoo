from django.contrib import admin
from django.urls import path, include  # include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls')),  # correct usage
]
