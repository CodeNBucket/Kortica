from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Club, Court, Reservation, PlayerPayment

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'is_manager', 'tennis_level', 'padel_level')
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'tennis_level', 'padel_level', 'profile_photo', 'is_manager', 'age', 'sex', 'favorite_clubs')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('phone_number', 'tennis_level', 'padel_level', 'profile_photo', 'is_manager', 'age', 'sex', 'favorite_clubs')
        }),
    )

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone_number', 'owner')

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'sport_type', 'surface_type', 'indoor', 'price')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('court', 'date', 'start_time', 'end_time', 'player_no', 'price', 'status')

@admin.register(PlayerPayment)
class PlayerPaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'player', 'amount_due', 'amount_paid', 'is_paid', 'method', 'paid_at')
