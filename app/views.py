from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app.models import Contact
from app.serializers import ContactSerializers


class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
