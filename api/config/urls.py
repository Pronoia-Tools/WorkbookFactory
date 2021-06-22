from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path("workbook-factory/admin/docs/", include("django.contrib.admindocs.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]


urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
