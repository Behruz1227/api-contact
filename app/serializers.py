from rest_framework.serializers import ModelSerializer

from app.models import Contact


class ContactSerializers(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"