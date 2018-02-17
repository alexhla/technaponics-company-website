from django.shortcuts import render

from contact.models import listemail

# Create your views here.

def index(request):
	return render(request, 'contact/contact.html')


