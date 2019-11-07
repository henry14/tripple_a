from django.conf import settings
from django.conf.urls import include, url as path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from material.frontend import urls as frontend_urls

admin.autodiscover()

urlpatterns = [
    path(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(r"^about/$", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("health.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path(r'^signupredirect/', TemplateView.as_view(template_name="admin/signupredirect.html"),
            name='sign_up_redirect'),
    # Your stuff: custom urls includes go here
    path(r'', include(frontend_urls)),
    path("ambulances/", include(("ambulances.urls", "ambulances"), namespace="ambulances")),
    path("consultancies/", include(("consultancies.urls", "consultancies"), namespace="consulancies")),
    path("pharmacies/", include(("pharmacies.urls", "pharmacies"), namespace="pharmacies")),
    path('services/', include(('health.services.urls', 'services'), namespace="services"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
