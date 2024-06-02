from django.conf import settings
from django.contrib import admin
from django.urls import path
# from django.views.generic import TemplateView

from django_project_reuse.views import robots_txt

# our admin/base_site.html override template also affects the title
admin.site.site_title = "REAL Django Admin"   # DEFAULT = "Django site admin"
admin.site.site_header = "Real Django Admin"  # DEFAULT = "Django Administration"
admin.site.index_title = "Site Admin Home"    # DEFAULT = "Site Administration"


urlpatterns = [
    path("robots.txt", robots_txt, name="robots_txt"),
    path(settings.ADMIN_URL, admin.site.urls),
    # path('', TemplateView.as_view(template_name='home.dtl'), name='home'),
]