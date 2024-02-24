"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('crumbs/', include('crumbs.urls')),
    path('people/', include('people.urls')),
]


# This is the landing page. Redirects the base URL '/' (or empty) to '/inventories/'.
# Taken from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# Leave the first parameter of the path function empty to imply '/'.
# If you write the first parameter as '/' Django will give you the following warning:
# ?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'.
# Remove this slash as it is unnecessary.
from django.views.generic.base import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/core/', permanent=True)),
]

# to serve media in the development server
# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)