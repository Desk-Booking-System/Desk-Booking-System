
from django.contrib import admin
from django.urls import include, path

# Need to add an API in the future

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('deskbooking.urls'))
]
