from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quans.urls')),
    #path('user/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('accounts.urls')),
    path('groups/', include('groups.urls')),
    path('search/', include('searching.urls')),
  
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/rest-auth/', include('rest_auth.urls')),#for log(in/out), passwordreset
    path('api/rest-auth/registration/', include('rest_auth.registration.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
