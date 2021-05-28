from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import BedSerializer, BookingSerializer
from .models import Bed, Booking
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class BedList(generics.ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('hospital', 'pin_code', 'available_from', 'critical_level')

class BedDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BookingList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer