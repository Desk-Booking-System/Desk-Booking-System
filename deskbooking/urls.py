from django.urls import path
from .views.LoginViews import user_login, deskbook
from .views.error_404_views import errorhandling

urlpatterns = [
 path('login/', user_login, name='login'),
 path('deskbook/', deskbook, name='deskbook'),
]

handler404 = errorhandling
