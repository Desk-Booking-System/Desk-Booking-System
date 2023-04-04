
from django.contrib import admin
from django.urls import include, path
#hello world
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('deskbooking.urls'))
]
