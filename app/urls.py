from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
