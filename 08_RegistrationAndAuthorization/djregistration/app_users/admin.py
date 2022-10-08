from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'date_of_birth', 'number_phone',
                    'number_published_news', 'verification_flag')
    list_filter = ('verification_flag',)

    actions = ['mark_as_verified', 'mark_as_not_verified']

    # list_editable = ('activity_flag',)
    # prepopulated_fields = {"slug": ("title",)}

    def mark_as_verified(self, request, obj):
        obj.update(verification_flag='Верифицирован')

    def mark_as_not_verified(self, request, obj):
        obj.update(verification_flag='Не верифицирован')

    mark_as_verified.short_description = 'Перевести в статус "Верифицирован"'
    mark_as_not_verified.short_description = 'Перевести в статус "Не верифицирован"'
