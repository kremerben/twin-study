from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings
from django.core.context_processors import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twin_study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'similarity.views.home', name='home'),
    url(r'^register/$', 'similarity.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),


    url(r'^profile/$', 'similarity.views.profile', name='profile'),
    url(r'^profile/(?P<user_id>\w+)/update/$', 'similarity.views.profile_update', name='profile_update'),


    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


    url(r'^add_image/$', 'similarity.views.add_image', name='add_image'),
    url(r'^view_gallery/$', 'similarity.views.view_gallery', name='view_gallery'),



    url(r'^test_post/$', 'similarity.views.test_post', name='test_post'),
    url(r'^questionnaire_view/$', 'similarity.views.questionnaire_view', name='questionnaire_view'),

)



#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
