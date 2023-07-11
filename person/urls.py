import imp
from django.conf.urls import url
from person.views import newPerson
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^new', login_required(newPerson) , name='index'),
]