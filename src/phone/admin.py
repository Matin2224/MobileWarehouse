from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Brand, Mobile

class MobileInline(admin.TabularInline):  # or use StackedInline for a vertical layout
    model = Mobile
    extra = 1  # Number of empty mobile forms to display
    can_delete = True
    fields = ('model', 'price', 'color', 'screen_size', 'availability_status', 'assembling_country')
    show_change_link = True  # Adds a link to edit the mobile entry from the Brand admin page

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')  # Fields to display in the admin list view
    search_fields = ('name', 'nationality')  # Enable search functionality
    inlines = [MobileInline]  # Add MobileInline to manage related mobiles from the Brand page
    ordering = ('name',)

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'availability_status')  # Fields to display in the admin list view
    list_filter = ('availability_status', 'brand')  # Add filters for easier navigation
    search_fields = ('model', 'brand__name')  # Enable search by model and brand name
    ordering = ('brand', 'price')
