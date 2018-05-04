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
	#queryset = Contact.objects.all()
	
	#serializer_class = ContactSerializer

	def get_object(self,pk):
		try:
			pdb.set_trace()
			return Contact.objects.get(pk=pk)
		except Contact.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		contatcts=self.get_object(pk)
		serializer=ContactSerializer(contatcts)
		return Response(serializer.data)