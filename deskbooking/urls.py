
from django.urls import path
from .views.LoginViews import user_login

urlpatterns = [
 path('login/', user_login, name='login'),
]