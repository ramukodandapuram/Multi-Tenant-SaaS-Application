from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from contacts.models import Contact
import pdb

class ContactSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contact




# Create your views here.

class ContactViewSet(APIView):
	queryset = Contact.objects.all()
	
	serializer_class = ContactSerializer

	
