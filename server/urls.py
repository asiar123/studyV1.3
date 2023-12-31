"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout_then_login
from user.views import Login
from matery.views import añadirMateria
from biology.views import añadirBiology

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('home.urls'))),
    path('user/',include(('user.urls','user'))),
    path('accounts/login/', Login.as_view(), name = 'login'),
    url(r'^logout/', logout_then_login, name='logout'),
    path('math/',añadirMateria.as_view(), name="matery"),
    url(r'^person/', include ('person.urls')),
    path('biology/',añadirBiology.as_view(), name="biology"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
