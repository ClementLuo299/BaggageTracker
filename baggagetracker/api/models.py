from django.db import models

# Create your models here.

#Database relations

#User, null=False is default
class Usr(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50,null=True, blank = True)
    lname = models.CharField(max_length=50)
    street = models.CharField(max_length=100,null=True, blank = True)
    country = models.CharField(max_length=100,null=True, blank = True)
    postal_code = models.CharField(max_length=50,null=True, blank = True)
    email = models.CharField(max_length=50,null=True, blank = True)

class Airline(models.Model):
    airline_name = models.CharField(max_length=100, primary_key=True)
    country_of_origin = models.CharField(max_length=50)

class Employee(models.Model):
    user_id = models.OneToOneField(Usr, on_delete=models.CASCADE, primary_key=True)
    employee_role = models.CharField(max_length=50, null=True, blank = True)
    password = models.CharField(max_length=50, null = True, blank = True)
    is_executive = models.BooleanField(default = False)
    airline = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True, blank = True)

class PhoneNumbers(models.Model):
    user = models.ForeignKey(Usr, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=30)
    class Meta:
        unique_together = ('user', 'phone_no')

class Customer(models.Model):
    passport_no = models.CharField(max_length=100, primary_key=True)
    country_citizenship = models.CharField(max_length=50, null=True, blank = True)
    user = models.OneToOneField(Usr, on_delete=models.CASCADE)

class Airport(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    airport_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50, null=True, blank = True)
    city = models.CharField(max_length=30, null=True, blank = True)

class Airplane(models.Model):
    registration_no = models.CharField(max_length=10, primary_key=True)
    airplane_type = models.CharField(max_length=30, null=True, blank = True)
    baggage_capacity = models.IntegerField(default = 0)
    current_payload = models.IntegerField(default = 0)
    airline = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True, blank = True)
    coordinates = models.CharField(max_length=20, null=True, blank = True)

class Loc(models.Model):
    location_name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=20)
    class Meta:
        unique_together = ('location_name', 'coordinates')

class SecurityCheckpoint(models.Model):
    location_name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=20)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('location_name', 'airport')

class StorageFacility(models.Model):
    location_name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=20)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('location_name', 'airport')

class BaggageCarousel(models.Model):
    carousel_number = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=20)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('carousel_number', 'airport')

class Itinerary(models.Model):
    booking_id = models.CharField(max_length=100)
    passport_no = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['booking_id', 'passport_no'], name='unique_booking_passport'
            )
        ]

class FlightLeg(models.Model):
    flight_id = models.CharField(max_length=20)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='origin_airport')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_airport')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['flight_id', 'airplane', 'origin', 'destination'], 
                name='unique_flight_leg'
            )
        ]

class ItineraryFlights(models.Model):
    booking_id = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(FlightLeg, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['booking_id', 'flight_id'], name='unique_booking_flight'
            )
        ]

class Baggage(models.Model):
    tracker_id = models.CharField(max_length=100)
    passport_no = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tracker_type = models.CharField(max_length=20, null=True, blank = True)
    booking_id = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    is_time_sensitive = models.BooleanField()
    is_hazardous = models.BooleanField()
    weight = models.DecimalField(max_digits=10, decimal_places=2, default = 0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tracker_id', 'passport_no'],
                name='unique_tracker_passport'
            )
        ]

class LocationUpdate(models.Model):
    update_time = models.DateTimeField()
    tracker_id = models.ForeignKey(Baggage, on_delete=models.CASCADE)
    location_name = models.ForeignKey(Loc, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['update_time', 'tracker_id'], name='unique_update_time_tracker'
            )
        ]

class Incident(models.Model):
    incident_id = models.CharField(max_length=100, primary_key=True)
    is_damaged = models.BooleanField()
    is_lost = models.BooleanField()
    is_delayed = models.BooleanField()
    incident_time = models.DateTimeField()
    incident_resolved = models.BooleanField()
    incident_description = models.TextField(null=True, blank = True)
    incident_location = models.ForeignKey(Loc, on_delete=models.CASCADE)

class IncidentEmployees(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('incident', 'user')

class Notification(models.Model):
    notification_id = models.CharField(max_length=100, primary_key=True)
    notification_content = models.TextField()
    notification_time = models.DateTimeField()

class NotificationSent(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Usr, on_delete=models.CASCADE)
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('notification', 'recipient')

class NotificationSubject(models.Model):
    notification_id = models.ForeignKey(Notification, on_delete=models.CASCADE)
    tracker_id = models.ForeignKey(Baggage, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['notification_id', 'tracker_id'], name='unique_notification_tracker'
            )
        ]
