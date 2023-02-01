from django.contrib import admin
from django.urls import path, include
from git_fork import urls as git_fork_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(git_fork_urls)),
]
