from django.urls import path
from . import views

from django.contrib.auth import views as view

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('log-in/', view.LoginView.as_view(template_name='userprofile/login.html'), name='log-in'),
    path('log-out/', view.LogoutView.as_view(), name='logout')
]
