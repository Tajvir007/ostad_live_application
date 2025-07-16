from django.contrib import admin

from .models import Club, UserProfile, User


class ClubAdmin(admin.ModelAdmin):
    list_display = ['name','id','created_by','modifyed_at','created_at']
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email 
        return super().save_model(request, obj, form, change)
    


admin.site.register(Club, ClubAdmin)

admin.site.register(UserProfile)
admin.site.register(User)
