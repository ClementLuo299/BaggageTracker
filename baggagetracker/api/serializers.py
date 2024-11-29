from rest_framework import serializers

#Import models
from .models import Usr 

#Define serializers
class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usr
        fields = ('user_id','fname','mname','lname','street','country','postal_code','email')