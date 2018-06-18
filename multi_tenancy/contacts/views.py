from rest_framework import serializers
from rest_framework import viewsets

from contacts.models import Contact
import pdb

class ContactSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contact




# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	
	serializer_class = ContactSerializer

	
