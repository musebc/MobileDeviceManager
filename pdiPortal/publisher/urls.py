from django.conf.urls import url
from . import views as publisher_views

urlpatterns = [
    url(r'^$', publisher_views.publisher, name='publisher'),
    url(r'^createApp/$', publisher_views.CreateApplication.as_view(), name="create-app"),
    url(
        r'^api/Application/(?P<_id>\w+)/$',
        publisher_views.GetApplication.as_view(),
        name="get-application-api"
        )
]
