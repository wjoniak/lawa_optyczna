from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('desk/', include('desk.urls')),
    path('admin/', admin.site.urls),
]