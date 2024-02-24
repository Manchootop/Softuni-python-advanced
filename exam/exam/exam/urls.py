from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam.main.urls')),
    path('car/', include('exam.cars.urls')),
    path('profile/', include('exam.profiles.urls')),
]
