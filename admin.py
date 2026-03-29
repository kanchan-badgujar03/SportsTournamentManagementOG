
from django.contrib import admin
from sports_app.models import Sport, Event, Player, Score, FootballGame, NewTeam, BasketballGame, NewGame


class FootballAdmin(admin.ModelAdmin):
    list_display=('Team_1_Name','Team_2_Name','Match_Date','Match_Time','Location','Final_Score','Remarks')
    search_fields = ('Team_1_Name', 'Team_2_Name', 'Location')
    list_filter = ('Match_Date', 'Location')
admin.site.register(FootballGame,FootballAdmin)

class BasketballAdmin(admin.ModelAdmin):
    list_display=('Team_1_Name','Team_2_Name','Match_Date','Match_Time','Location','Final_Score','Remarks')
    search_fields = ('Team_1_Name', 'Team_2_Name', 'Location')
    list_filter = ('Match_Date', 'Location')
admin.site.register(BasketballGame,BasketballAdmin)


@admin.register(NewTeam)
class NewTeamAdmin(admin.ModelAdmin):
    list_display = ("Team_Name", "Sport", "Coach_Name", "Number_of_Players")
    search_fields = ("Team_Name", "Coach_Name")

@admin.register(NewGame)
class NewGameAdmin(admin.ModelAdmin):
    list_display=('New_Game','Indoor_Outdoor')
    search_fields = ('New_Game', 'Indoor_Outdoor')
    

    


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'date', 'location')
    list_filter = ('sport', 'date')
    search_fields = ('name', 'location')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'coach', 'players_count')
    list_filter = ('sport',)
    search_fields = ('name', 'sport', 'coach', 'players_count')

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('event', 'team_name', 'points')
    list_filter = ('event',)
    search_fields = ('team_name',)
