
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
   
    #password
    #email
    #first_name
    #last_name 
    #username
    phone_number = models.CharField(max_length=20)
    tennis_level = models.IntegerField(default=1)
    padel_level = models.IntegerField(default=1)
    profile_photo = models.URLField(blank=True, null=True)
    is_manager = models.BooleanField(default=False)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    favorite_clubs = models.ManyToManyField('Club', related_name='favorited_by', blank=True)

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    email = models.EmailField(default="xyz@mail.com")
    phone_number = models.CharField(max_length=20,default=905312653668)
    rating = models.FloatField(default=0.0)
    photos = ArrayField(models.URLField(), blank=True, default=list)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clubs_owned')

class Court(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='courts')
    name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=10, choices=[('tennis', 'Tennis'), ('padel', 'Padel')],default='padel')
    surface_type = models.CharField(max_length=50)
    indoor = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_hours = models.JSONField(default=dict)
    photos = ArrayField(models.URLField(), blank=True, default=list)

class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='reservations')
    #players = models.ManyToManyField(User, related_name='reservations')
    #player_usernames = ArrayField(models.CharField(max_length=150), blank=True, default=list)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    player_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('booked', 'Booked'), ('cancelled', 'Cancelled'), ('completed', 'Completed')],
        default='booked'
    )

class PlayerPayment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='player_payments')
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount_due = models.DecimalField(max_digits=6, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    method = models.CharField(max_length=20, choices=[
        ('credit_card', 'Credit Card'),
        ('iyzico', 'Iyzico'),
        ('cash', 'Cash'),
        ('other', 'Other')
    ])
    #reservation_info = models.TextField(blank=True)
    paid_at = models.DateTimeField(blank=True, null=True)
