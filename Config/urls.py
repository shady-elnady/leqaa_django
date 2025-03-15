"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django import get_version
from django.contrib import admin
from django.urls import path, include  # , re_path
from django.utils.translation import gettext_lazy as _  # noqa: F401
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.views.decorators.cache import cache_page
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Api.restAPI.routes.router import router


api_version = "v1"

urlpatterns = [
    path(
        f"{api_version}/i18n/", include("django.conf.urls.i18n")
    ),  # for Multi Languages & Translation
    # Rest_Fram_Work
    path("api/", include("Api.urls", namespace="Api")),
    path(
        "api/",
        include(router.urls),
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += i18n_patterns(
    path(
        "jsi18n/",
        cache_page(86400, key_prefix="jsi18n-%s" % get_version())(
            JavaScriptCatalog.as_view()
        ),
        name="javascript-catalog",
    ),
    # path("", include("django.contrib.auth.urls")), # include all auth views
    # path("", include("Logs.urls", namespace="Logs")),
    path("", include("User.urls", namespace="User")),
    # path(
    #     "templated_email",
    #     include("templated_email.urls", namespace="templated_email"),
    # ),
    # Admin
    path("admin/", admin.site.urls),
    # debug toolbar URLS
    path("__debug__/", include(debug_toolbar.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()


"""

https://medium.com/@akshatgadodia/a-guide-to-globalizing-your-django-application-internationalization-and-localization-fcee3e22b883

"""
