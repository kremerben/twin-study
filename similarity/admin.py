from django.contrib import admin

# Register your models here.

from models import *



class UserImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'subject_id', 'gallery_name')
    list_filter = ('subject_id', 'gallery_name',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('user', 'gallery_name')
    list_filter = ('user', 'gallery_name',)



admin.site.register(User)
admin.site.register(Questionnaire)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Gallery, GalleryAdmin)

