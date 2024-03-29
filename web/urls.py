"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coreapp.urls")),
    path("fbase1/", include("fbase1.urls")),
    path("fbase2/", include("fbase2.urls")),
    path("fbase3/", include("fbase3.urls")),
    path("cbase1/", include("cbase1.urls")),
    path("cbase2/", include("cbase2.urls")),
    path("cbase3/", include("cbase3.urls")),
    path("api/1.0/", include("apis1.urls")),
    path("api/2.0/", include("apis2.urls")),
    path("api/3.0/", include("apis3.urls")),
    path("api/4.0/", include("apis4.urls")),
]
