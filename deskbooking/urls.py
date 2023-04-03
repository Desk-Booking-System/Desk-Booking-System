from django.urls import path
from .views.LoginViews import user_login
from .views.error_404_views import errorhandling

urlpatterns = [
 path('login/', user_login, name='login'),
]

handler404 = errorhandling
