from django.conf.urls import url
from . import views

#TEMPLAYE URL
app_name='basic_app'

urlpatterns= [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
