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


from django.urls import include, path
from django.views.generic import TemplateView

# ------------------------------------------------------------------------------
# still has to be in root URLconf for now
# https://docs.djangoproject.com/en/5.1/topics/http/urls/#error-handling

from django.conf.urls import handler400, handler403, handler404, handler500
from django_project_reuse.views import error_400, error_403, error_404, error_500

handler400 = error_400
handler403 = error_403
handler404 = error_404  # must return status=404 for APPEND_SLASH to work
handler500 = error_500

# ------------------------------------------------------------------------------

urlpatterns = [
    path('', include('django_project_reuse.urls')),

    path('', TemplateView.as_view(template_name='home.dtl'), name='home'),
]