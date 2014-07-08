from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from people.views import HomePageView, UserViewSet, HomePageRedirectView


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
                       url(r'^$', HomePageRedirectView.as_view()),
                       url(r'^api/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include(
                           'rest_framework.urls', namespace='rest_framework')),
                       url(r'^home/', HomePageView.as_view(), name='home'),
                       )
