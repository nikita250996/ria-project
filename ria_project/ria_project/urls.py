"""ria_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from application import routers as app_routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='APP API')


urlpatterns = [
    path('', include('application.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(app_routers.router.urls)),
    path('schema/', schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
