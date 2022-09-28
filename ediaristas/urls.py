from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('api/', include('api.urls')),
]
