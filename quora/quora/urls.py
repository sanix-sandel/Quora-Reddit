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

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
