from django.contrib import admin

from .models import Contact,Hire

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']

@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display=['id','jobt','describe','skills','exp','cont','email']