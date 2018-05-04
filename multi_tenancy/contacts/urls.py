from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter
from contacts.views import ContactViewSet

router = DefaultRouter()
router.register(r'contacts',ContactViewSet)

urlpatterns = [
	url(r'^',include(router.urls)),
	]
