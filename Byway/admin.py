from django.contrib import admin
from .models import Category,Course

# Register the Category model with the admin interface
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image') 
    search_fields = ('title',)  
    list_filter = ('title',)  


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('Title','description','rating','duration','lectures','autherImg', 'auther', 'language','thumbnailImg', 'Ogprice', 'Offprice')  # Customize the fields to display in the list
    search_fields = ('Title', 'auther')  # Add search functionality
    list_filter = ('Title',)  # Add filters
