from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display    = ('title','slug','author','published','status')
    list_filter = ('status','created','author','published')
    date_hierarchy = 'published'
    search_fields   = ('title','content') 
    prepopulated_fields = {'slug':('title',)}