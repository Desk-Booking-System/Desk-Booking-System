from django.urls import path
from .views.LoginViews import user_login
from .views.error_404_views import errorhandling
from .views.DeskViews import add_desk, Desks
urlpatterns = [
 path('', user_login, name='login'),
 path('deskbook/', Desks, name='deskbook'),
#  path('deskbook/<desk_id>', Desk_Update, name='deskbook'),
 
]

handler404 = errorhandling
