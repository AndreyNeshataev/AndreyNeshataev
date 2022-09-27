from django.contrib import admin
from .models import Restaurant, Waiter


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'director', 'chef', 'phone')
    fieldsets = (

        ('Основные данные', {
            'fields': ('name', 'description')
        }),

        ('Дополнительные данные', {
            'fields': ('director', 'chef', "count_of_employers"),
            'description': 'Дополнительные данные о ресторане',
            'classes': ['collapse']
        }),

        ('Контактные данные', {
            'fields': ('phone', 'country', 'city', 'street', 'house'),
            'description': 'Контактные данные о ресторане'
        }),

        ('Данные о наличии сервисов', {
            'fields': (
            'serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_donats', 'serves_coffee'),
            'description': 'Дополнительные данные о ресторане',
            'classes': ['collapse']
        })
    )


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'sex', 'restaurant')
    # list_editable = ('user_name', 'commentary')
    # search_fields = ('name',)
    fieldsets = (

        ('Основные данные', {
            'fields': ('first_name', 'last_name', 'age', 'sex')
        }),

        ('Адрес', {
            'fields': ('country', 'city', 'street', 'house'),
            'description': 'Информация о месте проживания работника'
        }),

        ('Дополнительные данные', {
            'fields': ('seniority', 'education', 'cources'),
            'description': 'Дополнительные данные о работнике',
            'classes': ['collapse']
        })
    )
