from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^on/$', views.MovementDirection.as_view({'get':'on'})),
    url(r'^off/$', views.MovementDirection.as_view({'get':'off'})),
    url(r'^forward/$', views.MovementDirection.as_view({'get':'forward'})),
    url(r'^backwards/$', views.MovementDirection.as_view({'get':'backwards'})),
    url(r'^left/$', views.MovementDirection.as_view({'get':'left'})),
    url(r'^right/$', views.MovementDirection.as_view({'get':'right'})),
]

