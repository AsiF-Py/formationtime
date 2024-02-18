from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('home/',views.home,name='home'),
    path("register/", views.register),
    path('login/',views.login_view,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view),
    path('register/', views.register, name='register'),
    path('dashboard/',views.dashboard)
]