from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^game/home$', views.game_home),
    url(r'^game/animals$', views.animal),
    url(r'^process_result$', views.process_result),
    # url(r'^game/view_result$', views.result),
    url(r'^game/(?P<animal>\w+)$', views.animal_size),
    url(r'^game/(?P<animal>\w+)/(?P<size>\d+)$', views.animal_age),
    url(r'^game/(?P<animal>\w+)/(?P<size>\d+)/(?P<age>\d+)$', views.animal_energy),
    url(r'^game/(?P<animal>\w+)/(?P<size>\d+)/(?P<age>\d+)/(?P<energy>\d+)$', views.animal_friendly),
    url(r'^game/(?P<animal>\w+)/(?P<size>\d+)/(?P<age>\d+)/(?P<energy>\d+)/(?P<friendly>\d+)$', views.find_animal),
]
