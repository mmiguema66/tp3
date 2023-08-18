
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from proyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
    path('welcome/', bienvenida),
    path('welcome2/', bienvenida_html),
    path('welcome3/', bienvenida_template),
    

    
    path('saludar/<nombre>/', saludar),
]
