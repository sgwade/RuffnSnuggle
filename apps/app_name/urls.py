from django.conf.urls import url
from . import views 
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^caring$', views.caring),
    url(r'^all_dogs$', views.all_dogs),
    url(r'^all_cats$', views.all_cats),
    url(r'^signin_page$', views.log_or_reg),
    url(r'^logout$', views.logout),
    url(r'^register_process$', views.register_process), 
    url(r'^dashboard$', views.dashboard), 
    url(r'^login_process$', views.login_process),
    url(r'^this_animal/(?P<pets_id>\d+)$', views.this_animal),
    url(r'^favorites/(?P<user_id>\d+)/(?P<pets_id>\d+)$', views.favorites),
    url(r'^delete/(?P<pets_id>\d+)$', views.delete),
    url(r'^subappt$', views.subappt),
    url(r'^alert$', views.alert),
]
