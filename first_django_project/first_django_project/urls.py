from django.contrib import admin
from django.urls import include, path
from blogs import views

urlpatterns = [
    path('', include('blogs.routes')),
    path('blogs/', include('blogs.routes')),
    # path('index/', include('blogs.urls')),
    # path('admin/', admin.site.urls),
]
