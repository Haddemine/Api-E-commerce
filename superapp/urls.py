from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ecommerce import views
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView

urlpatterns = [
    path('',views.index),
    path('superapp/', admin.site.urls),
    path('apis/', include('apis.urls', namespace='apis')),
    # path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    # path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('ecommerce/', include('ecommerce.urls', namespace='ecommerce'))
]
