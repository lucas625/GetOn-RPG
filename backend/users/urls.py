from django.urls import path
from django.conf.urls import include
from users.views import User

app_name = 'users'

urlpatterns = [
    path('api/{}/'.format(app_name), User.as_view(), name='indexUser'),
    path('api/{}/test/'.format(app_name), User.as_view(), name='indexUser'),
]
