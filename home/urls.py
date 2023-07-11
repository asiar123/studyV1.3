from django.conf.urls import url
from home.views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(index) , name='home'),
]