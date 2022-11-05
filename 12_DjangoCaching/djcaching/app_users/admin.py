from django.contrib import admin
from app_users.models import Profile, PurchaseHistory


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'date_of_birth', 'number_phone', 'balance')
    list_filter = ('user', 'city')


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'goods', 'purchase_date',)
    list_filter = ('user', 'goods', 'purchase_date')

