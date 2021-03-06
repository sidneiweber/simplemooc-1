from django.conf.urls import include, url
from django.contrib import admin
from simplemooc.core import urls as core_urls
from simplemooc.courses import urls as courses_url

urlpatterns = [
    url(r'^', include(core_urls), name='core'),
    url(r'^courses/', include(courses_url), name='courses'),
    url(r'^admin/', include(admin.site.urls)),
]
