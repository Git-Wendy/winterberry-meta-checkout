from django.urls import include, path
from checkout.views import HealthView

urlpatterns = [
    path("", HealthView.as_view(), name="health"),
    path("", include("checkout.urls")),
]
