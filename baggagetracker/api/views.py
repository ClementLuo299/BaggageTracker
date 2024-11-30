from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    UsrSerializer,
    AirlineSerializer,
    EmployeeSerializer,
    PhoneNumbersSerializer,
    CustomerSerializer,
    AirportSerializer,
    AirplaneSerializer,
    LocSerializer,
    SecurityCheckpointSerializer,
    StorageFacilitySerializer,
    BaggageCarouselSerializer,
    ItinerarySerializer,
    FlightLegSerializer,
    ItineraryFlightsSerializer,
    BaggageSerializer,
    LocationUpdateSerializer,
    IncidentSerializer,
    IncidentEmployeesSerializer,
    NotificationSerializer,
    NotificationSentSerializer,
    NotificationSubjectSerializer
)

from .models import (
    Usr,
    Airline,
    Employee,
    PhoneNumbers,
    Customer,
    Airport,
    Airplane,
    Loc,
    SecurityCheckpoint,
    StorageFacility,
    BaggageCarousel,
    Itinerary,
    FlightLeg,
    ItineraryFlights,
    Baggage,
    LocationUpdate,
    Incident,
    IncidentEmployees,
    Notification,
    NotificationSent,
    NotificationSubject
)

# View to create a new Usr
class UsrView(generics.CreateAPIView):
    queryset = Usr.objects.all()
    serializer_class = UsrSerializer

# View to create a new Air  line
class AirlineView(generics.CreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

# View to create a new Employee
class EmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# View to create a new PhoneNumbers
class PhoneNumbersView(generics.CreateAPIView):
    queryset = PhoneNumbers.objects.all()
    serializer_class = PhoneNumbersSerializer

# View to create a new Customer
class CustomerView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# View to create a new Airport
class AirportView(generics.CreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

# View to create a new Airplane
class AirplaneView(generics.CreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

# View to create a new Loc
class LocView(generics.CreateAPIView):
    queryset = Loc.objects.all()
    serializer_class = LocSerializer

# View to create a new SecurityCheckpoint
class SecurityCheckpointView(generics.CreateAPIView):
    queryset = SecurityCheckpoint.objects.all()
    serializer_class = SecurityCheckpointSerializer

# View to create a new StorageFacility
class StorageFacilityView(generics.CreateAPIView):
    queryset = StorageFacility.objects.all()
    serializer_class = StorageFacilitySerializer

# View to create a new BaggageCarousel
class BaggageCarouselView(generics.CreateAPIView):
    queryset = BaggageCarousel.objects.all()
    serializer_class = BaggageCarouselSerializer

# View to create a new Itinerary
class ItineraryView(generics.CreateAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

# View to create a new FlightLeg
class FlightLegView(generics.CreateAPIView):
    queryset = FlightLeg.objects.all()
    serializer_class = FlightLegSerializer

# View to create a new ItineraryFlights
class ItineraryFlightsView(generics.CreateAPIView):
    queryset = ItineraryFlights.objects.all()
    serializer_class = ItineraryFlightsSerializer

# View to create a new Baggage
class BaggageView(generics.CreateAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer

# View to create a new LocationUpdate
class LocationUpdateView(generics.CreateAPIView):
    queryset = LocationUpdate.objects.all()
    serializer_class = LocationUpdateSerializer

# View to create a new Incident
class IncidentView(generics.CreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

# View to create a new IncidentEmployees
class IncidentEmployeesView(generics.CreateAPIView):
    queryset = IncidentEmployees.objects.all()
    serializer_class = IncidentEmployeesSerializer

# View to create a new Notification
class NotificationView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# View to create a new NotificationSent
class NotificationSentView(generics.CreateAPIView):
    queryset = NotificationSent.objects.all()
    serializer_class = NotificationSentSerializer

# View to create a new NotificationSubject
class NotificationSubjectView(generics.CreateAPIView):
    queryset = NotificationSubject.objects.all()
    serializer_class = NotificationSubjectSerializer
