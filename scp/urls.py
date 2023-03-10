"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
#import debug_toolbar

from blog.sitemaps import PostSitemap
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path("summernote/", include("django_summernote.urls")),
#    path('__debug__/', include(debug_toolbar.urls)),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Safer City Project'
admin.site.index_title = 'SCP Admin'
admin.site.site_title = 'SCP Admin'
