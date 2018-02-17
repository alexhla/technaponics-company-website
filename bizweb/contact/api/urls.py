from rest_framework import routers
from contact.api.views import (listemailViewSet, formcontactViewSet)

router = routers.SimpleRouter()	# Includes routes for the standard set of "list, create, retrieve, update, partial_update, destroy"
router.register(r'listemail', listemailViewSet)	# where, listemail is the URL prefix and listemailViewSet is the viewset class
router.register(r'formcontact', formcontactViewSet, base_name='formcontact')


urlpatterns = []
urlpatterns += router.urls