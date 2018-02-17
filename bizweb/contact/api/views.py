
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

# Import Local Models & Serializers
from contact.models import (listemail, formcontact)
from contact.api.serializers import (listemailSerializer, formcontactSerializer)

# Create your views here.
class listemailViewSet(ModelViewSet):
	http_method_names =  ['post']
	serializer_class = listemailSerializer
	queryset = listemail.objects.none()

class formcontactViewSet(ModelViewSet):
	http_method_names =  ['post']
	serializer_class = formcontactSerializer
	queryset = formcontact.objects.none()