from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import ContactView

router = DefaultRouter()
router.register('contact', ContactView)


urlpatterns = [
    path('', include(router.urls)),
]
