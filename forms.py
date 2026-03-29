
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Sport, Event, Player, Score, FootballGame, NewTeam, BasketballGame,  NewGame

class FootballGameForm(forms.ModelForm):
    class Meta:
        model = FootballGame
        fields = '__all__'

class BasketballGameForm(forms.ModelForm):
    class Meta:
        model = BasketballGame
        fields = '__all__'

class NewGameForm(forms.ModelForm):
    class Meta:
        model = NewGame
        fields = '__all__'

class NewTeamForm(forms.ModelForm):
    class Meta:
        model = NewTeam
        fields = ["Team_Name", "Sport", "Coach_Name", "Number_of_Players"]

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name', 'category', 'description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['sport', 'name', 'date', 'location']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'sport', 'coach', 'players_count']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['event', 'team_name', 'points']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username', 'autocomplete': 'off'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'autocomplete': 'new-password'
    }))

class ScheduleUploadForm(forms.Form):
    file = forms.FileField()

    
