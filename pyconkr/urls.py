"""pyconkr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

import sponsor.routers
import status.urls
import ticket.urls
import payment.urls

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("admin/", admin.site.urls),
    path("sponsors", include(sponsor.routers.get_router().urls)),
    path("programs/", include("program.urls")),
    path("statuses/", include(status.urls)),
    path("tickets/", include(ticket.urls)),
    path("payments/", include(payment.urls)),
    path("", include("account.urls")),
]

if settings.DEBUG is True:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path(
            "api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
