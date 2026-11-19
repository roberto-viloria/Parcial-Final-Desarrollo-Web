
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'programas/',
        include(("myapp.urls", "programas"), namespace="programas"),
    ),
    # INCLUIR LAS RUTAS HIJAS
    path('profiles/', include("myapp.urls")),
]
