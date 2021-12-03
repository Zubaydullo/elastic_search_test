from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import BookDocumentView

router = DefaultRouter()
books = router.register(r"books", BookDocumentView, basename="bookdocument")


urlpatterns = [
    url(r"^", include(router.urls)),
]
