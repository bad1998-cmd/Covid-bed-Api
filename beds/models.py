from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bed(models.Model):
    hospital = models.CharField(max_length=250)
    pin_code = models.CharField(max_length=6)
    available_from = models.DateField(auto_now=False, auto_now_add=False)
    available_till = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    critical_level = models.CharField(max_length=250, null=True, blank=True)
    #occupant = *look at booking model*

    def __str__(self):
        return f"1 Bed in {self.hospital}, available from {self.available_from} to {self.available_till}" 
    
class Booking(models.Model):
   patient_name = models.CharField(max_length=250)
   bed = models.OneToOneField(Bed, related_name='occupant', on_delete=models.CASCADE)
   book_from = models.DateField(auto_now=False, auto_now_add=False)
   book_till = models.DateField(auto_now=False, auto_now_add=False)

   def __str__(self):
       return self.patient_name