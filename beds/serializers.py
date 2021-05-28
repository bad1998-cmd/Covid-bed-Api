from rest_framework import serializers
from .models import Bed, Booking

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'hospital', 'pin_code', 'available_from', 'available_till', 'critical_level', 'occupant')
        model = Bed

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'patient_name', 'bed', 'book_from', 'book_till')
        model = Booking