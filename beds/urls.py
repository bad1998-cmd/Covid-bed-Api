from django.urls import path
from .views import BedList, BedDetail, BookingList, BookingCreate, BookingDetail

urlpatterns = [
    path('<int:pk>', BedDetail.as_view()),
    path('', BedList.as_view()),
    path('bookings', BookingList.as_view()),
    path('bookings/create', BookingCreate.as_view()),
    path('bookings/<int:pk>', BookingDetail.as_view())

]
