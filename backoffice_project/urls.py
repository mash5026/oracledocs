from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



# admin.autodiscover()
# reporting.autodiscover() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-child-locations/', include('backoffice.urls')),
    path('', include('backoffice.urls')),
    path('select2/', include('django_select2.urls')),
    path('documents/', include('metadata.urls')),

    #path('explorer/', include('explorer.urls')),
    #path('adminactions/', include('adminactions.urls')),
    #path('reporting/', include('reporting.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)