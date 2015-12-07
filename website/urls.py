from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
    url(r'^topic/(?P<id>\d+)$', 'getPosts', name='topic'),
    url(r'^topic/(?P<id>\d+)/post/(?P<post_id>\d+)$', 'getPost', name='post'),
    url(r'^random$', 'randomPosts', name='random'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

