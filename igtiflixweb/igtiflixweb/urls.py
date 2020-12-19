from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
urlpatterns = [
    path(route='', view=include("principal.urls")),
    path('admin/', admin.site.urls),
    path(route='principal/', view=include("principal.urls")),
    path(route='genero/', view=include("genero.urls")),
    path(route='serie/', view=include("serie.urls")),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
]
