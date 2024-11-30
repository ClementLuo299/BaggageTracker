#import
from rest_framework import serializers
from .models import Usr, Airline, Employee, PhoneNumbers, Customer, Airport, Airplane, Loc, SecurityCheckpoint, StorageFacility, BaggageCarousel, Itinerary, FlightLeg, ItineraryFlights, Baggage, LocationUpdate, Incident, IncidentEmployees, Notification, NotificationSent, NotificationSubject

# Serializer for Usr model
class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usr
        fields = ('user_id', 'fname', 'mname', 'lname', 'street', 'country', 'postal_code', 'email')

# Serializer for Airline model
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('airline_name', 'country_of_origin')

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    user_id = UsrSerializer()  # Nested UsrSerializer
    airline = AirlineSerializer()  # Nested AirlineSerializer

    class Meta:
        model = Employee
        fields = ('user_id', 'employee_role', 'airline')

# Serializer for PhoneNumbers model
class PhoneNumbersSerializer(serializers.ModelSerializer):
    user = UsrSerializer()  # Nested UsrSerializer

    class Meta:
        model = PhoneNumbers
        fields = ('user', 'phone_no')

# Serializer for Customer model
class CustomerSerializer(serializers.ModelSerializer):
    user = UsrSerializer()  # Nested UsrSerializer

    class Meta:
        model = Customer
        fields = ('passport_no', 'country_citizenship', 'user')

# Serializer for Airport model
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('code', 'airport_name', 'country', 'city')

# Serializer for Airplane model
class AirplaneSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()  # Nested AirlineSerializer

    class Meta:
        model = Airplane
        fields = ('registration_no', 'airplane_type', 'baggage_capacity', 'current_payload', 'airline', 'destination', 'coordinates')

# Serializer for Loc model
class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc
        fields = ('location_name', 'coordinates')

# Serializer for SecurityCheckpoint model
class SecurityCheckpointSerializer(serializers.ModelSerializer):
    airport = AirportSerializer()  # Nested AirportSerializer

    class Meta:
        model = SecurityCheckpoint
        fields = ('location_name', 'coordinates', 'airport')

# Serializer for StorageFacility model
class StorageFacilitySerializer(serializers.ModelSerializer):
    airport = AirportSerializer()  # Nested AirportSerializer

    class Meta:
        model = StorageFacility
        fields = ('location_name', 'coordinates', 'airport')

# Serializer for BaggageCarousel model
class BaggageCarouselSerializer(serializers.ModelSerializer):
    airport = AirportSerializer()  # Nested AirportSerializer

    class Meta:
        model = BaggageCarousel
        fields = ('carousel_number', 'coordinates', 'airport')

# Serializer for Itinerary model
class ItinerarySerializer(serializers.ModelSerializer):
    passport_no = CustomerSerializer()  # Nested CustomerSerializer

    class Meta:
        model = Itinerary
        fields = ('booking_id', 'passport_no')

# Serializer for FlightLeg model
class FlightLegSerializer(serializers.ModelSerializer):
    airplane = AirplaneSerializer()  # Nested AirplaneSerializer
    origin = AirportSerializer()  # Nested AirportSerializer
    destination = AirportSerializer()  # Nested AirportSerializer

    class Meta:
        model = FlightLeg
        fields = ('flight_id', 'airplane', 'origin', 'destination', 'departure_time', 'arrival_time')

# Serializer for ItineraryFlights model
class ItineraryFlightsSerializer(serializers.ModelSerializer):
    booking_id = ItinerarySerializer()  # Nested ItinerarySerializer
    flight_id = FlightLegSerializer()  # Nested FlightLegSerializer

    class Meta:
        model = ItineraryFlights
        fields = ('booking_id', 'flight_id')

# Serializer for Baggage model
class BaggageSerializer(serializers.ModelSerializer):
    passport_no = CustomerSerializer()  # Nested CustomerSerializer
    booking_id = ItinerarySerializer()  # Nested ItinerarySerializer

    class Meta:
        model = Baggage
        fields = ('tracker_id', 'passport_no', 'tracker_type', 'booking_id', 'is_time_sensitive', 'is_hazardous')

# Serializer for LocationUpdate model
class LocationUpdateSerializer(serializers.ModelSerializer):
    tracker_id = BaggageSerializer()  # Nested BaggageSerializer
    location_name = LocSerializer()  # Nested LocSerializer

    class Meta:
        model = LocationUpdate
        fields = ('update_time', 'tracker_id', 'location_name')

# Serializer for Incident model
class IncidentSerializer(serializers.ModelSerializer):
    incident_location = LocSerializer()  # Nested LocSerializer

    class Meta:
        model = Incident
        fields = ('incident_id', 'is_damaged', 'is_lost', 'is_delayed', 'incident_time', 'incident_resolved', 'incident_description', 'incident_location')

# Serializer for IncidentEmployees model
class IncidentEmployeesSerializer(serializers.ModelSerializer):
    incident = IncidentSerializer()  # Nested IncidentSerializer
    user = EmployeeSerializer()  # Nested EmployeeSerializer

    class Meta:
        model = IncidentEmployees
        fields = ('incident', 'user')

# Serializer for Notification model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('notification_id', 'notification_content', 'notification_time')

# Serializer for NotificationSent model
class NotificationSentSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()  # Nested NotificationSerializer
    recipient = UsrSerializer()  # Nested UsrSerializer
    sender = EmployeeSerializer()  # Nested EmployeeSerializer

    class Meta:
        model = NotificationSent
        fields = ('notification', 'recipient', 'sender')

# Serializer for NotificationSubject model
class NotificationSubjectSerializer(serializers.ModelSerializer):
    notification_id = NotificationSerializer()  # Nested NotificationSerializer
    tracker_id = BaggageSerializer()  # Nested BaggageSerializer

    class Meta:
        model = NotificationSubject
        fields = ('notification_id', 'tracker_id')
