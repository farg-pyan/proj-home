"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django_project.views_extra import error_400, error_403, error_404, error_500
from django_project.views_extra import robots_txt


handler400 = error_400
handler403 = error_403
handler404 = error_404  # must return status=404 for APPEND_SLASH to work
handler500 = error_500

# our admin/base_site.html override template also affects the title
admin.site.site_title = "REAL Django Admin"   # DEFAULT = "Django site admin"
admin.site.site_header = "Real Django Admin"  # DEFAULT = "Django Administration"
admin.site.index_title = "Site Admin Home"    # DEFAULT = "Site Administration"


urlpatterns = [
    path("robots.txt", robots_txt, name="robots_txt"),
    path(settings.ADMIN_URL, admin.site.urls),
    path('', TemplateView.as_view(template_name='home.dtl'), name='home'),
]