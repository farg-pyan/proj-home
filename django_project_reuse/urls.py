from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django_project_reuse.views import error_400
from django_project_reuse.views import error_403
from django_project_reuse.views import error_404
from django_project_reuse.views import error_500
from django_project_reuse.views import robots_txt

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