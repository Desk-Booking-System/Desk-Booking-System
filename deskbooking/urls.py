from django.urls import path
from .views.LoginViews import user_login, deskbook
from .views.error_404_views import errorhandling
from .views.DeskViews import add_desk

urlpatterns = [
 path('login/', user_login, name='login'),
 path('deskbook/', deskbook, name='deskbook'),
 path('add/', add_desk, name='add'),
]

handler404 = errorhandling
