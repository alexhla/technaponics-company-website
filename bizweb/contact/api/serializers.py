from rest_framework.serializers import ModelSerializer
from contact.models import (listemail, formcontact)

class listemailSerializer(ModelSerializer):
	class Meta:
		model = listemail
		fields = ('id','email')

class formcontactSerializer(ModelSerializer):
	class Meta:
		model = formcontact
		fields = ('id','name', 'email', 'msg')