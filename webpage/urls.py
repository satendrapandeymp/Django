from django.conf.urls import url
from . import views
from .models import User
#Defining URLs related to webpage
app_name = 'webpage'

db = User.objects.all()

urlpatterns = [

    url(r'^$', views.index , name='index'),

    url(r'^(?P<names>[a-z,A-Z]+)/$', views.Profile , name='profile'),

    url(r'^user/Details/$', views.Details , name='Details'),

    url(r'^(?P<names>[a-z,A-Z]+)/Images$', views.Images , name='Images'),

    url(r'^user/(?P<pk>[0-9]+)/AddImage/$', views.AddImage.as_view() , name='AddImage'),

    url(r'^user/Massages/$', views.Massages , name='Massages'),

    url(r'^user/AddMassages/$', views.AddMassage.as_view() , name='AddMassages'),

    url(r'^(?P<names>[a-z,A-Z]+)/Data$', views.Data , name='Data'),

    url(r'^user/(?P<pk>[0-9]+)/AddData/$', views.AddData.as_view() , name='AddData'),

    url(r'^user/reg/$', views.UserFormView.as_view() , name='reg'),

    url(r'^user/login/$', views.login_user, name='login'),

    url(r'^user/logout/$', views.logout_user, name='logout'),

    url(r'^user/Add/$', views.AddUser.as_view() , name='AddUser'),

    url(r'^user/(?P<pk>[0-9]+)/$', views.UpdateUser.as_view() , name='UpdateUser'),

    url(r'^user/(?P<pk>[0-9]+)/Delete/$', views.DeleteUser.as_view() , name='DeleteUser'),



]
