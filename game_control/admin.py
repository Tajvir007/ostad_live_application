from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from .models import GameCategory, Tournament, Game, GameQuestion, QuestionAnswer




class GameCategoryAdmin(admin.ModelAdmin):

    list_display = ['name','id','created_by', 'modifyed_at','created_at']
    fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email 
        return super().save_model(request, obj, form, change)
    
class GameAdmin(admin.ModelAdmin):

    list_display = ['name','id','created_by', 'modifyed_at','created_at']
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email 
        return super().save_model(request, obj, form, change)
    


class TournamentAdmin(admin.ModelAdmin):

    list_display = ['name','id','created_by', 'modifyed_at','created_at']
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email 
        return super().save_model(request, obj, form, change)

admin.site.register(GameCategory, GameCategoryAdmin)
admin.site.register(Tournament,TournamentAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameQuestion)
admin.site.register(QuestionAnswer)

