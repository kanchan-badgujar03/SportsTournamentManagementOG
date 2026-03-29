import openpyxl
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import MatchSchedule
from sports_app.models import Sport, Event, Player, Score, FootballGame, NewTeam, BasketballGame, NewGame
from .forms import SportForm, EventForm, PlayerForm, ScoreForm, FootballGameForm, NewTeamForm, BasketballGameForm, NewGameForm, ScheduleUploadForm

def football_view(request):
    if request.method == 'POST':
        form = FootballGameForm(request.POST)
        if form.is_valid():
            form.save()   # ✅ saves data to DB
            return redirect('football')  # reload form or redirect to success page
    else:
        form = FootballGameForm()

    return render(request, 'football.html', {'form': form})

def fdetails(request):
    t = FootballGame.objects.all().order_by('id')
    return render(request, 'fdetails.html',{'t': t})

def basketball_view(request):
    if request.method == 'POST':
        form = BasketballGameForm(request.POST)
        if form.is_valid():
            form.save()   # ✅ saves data to DB
            return redirect('basketball')  # reload form or redirect to success page
    else:
        form = BasketballGameForm()

    return render(request, 'basketball.html', {'form': form})

def bdetails(request):
    t = BasketballGame.objects.all().order_by('id')
    return render(request, 'bdetails.html',{'t': t})

def manage_teams(request):
    teams = NewTeam.objects.all().order_by('id')  # Fetch all saved teams
    return render(request, 'manage_teams.html', {'teams': teams})


def add_team(request):
    if request.method == "POST":
        form = NewTeamForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Saves team to database
            return redirect('add_team')  # reload page or redirect somewhere else
    else:
        form = NewTeamForm()
    return render(request, "add_team.html", {"form": form})

def added_sports(request):
    t = NewGame.objects.all().order_by('id')  # Fetch all saved teams
    return render(request, 'added_sports.html', {'t': t})


def add_sports(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Saves team to database
            return redirect('add_sports')  # reload page or redirect somewhere else
    else:
        form = NewGameForm()
    return render(request, "add_sports.html", {"form": form})





def home(request):
    sports = Sport.objects.all().order_by('name')
    events = Event.objects.select_related('sport').order_by('date')[:10]
    return render(request, 'home.html', {'sports': sports, 'events': events})

# Lists




def sports_list(request):
    items = Sport.objects.all().order_by('name')
    return render(request, 'sports_list.html', {'items': items})

def events_list(request):
    items = Event.objects.select_related('sport').order_by('-date')
    return render(request, 'events_list.html', {'items': items})

def players_list(request):
    items = Player.objects.select_related('sport').order_by('name')
    return render(request, 'players_list.html', {'items': items})

def scores_list(request):
    items = Score.objects.select_related('event').order_by('-event__date')
    return render(request, 'scores_list.html', {'items': items})

# Create forms
def sport_create(request):
    if request.method == 'POST':
        form = SportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sports_list')
    else:
        form = SportForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Sport'})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')
    else:
        form = EventForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Event'})

def is_admin(user):
    return user.is_superuser

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials or not admin."})
    
    return render(request, "admin_login.html")

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

def score_create(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scores_list')
    else:
        form = ScoreForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Score'})

def dashboard(request):
    return render(request, 'dashboard.html')


def add_game(request):
    return render(request, 'add_game.html')


def upload_page(request):
    if request.method == "POST":
        form = ScheduleUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["file"]

            # Load workbook
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            # Clear old schedule (optional)
            MatchSchedule.objects.all().delete()

            # Iterate through rows (skip header)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                team1, team2, match_date, match_time, venue = row
                MatchSchedule.objects.create(
                    team1=team1,
                    team2=team2,
                    match_date=match_date,
                    match_time=match_time,
                    venue=venue,
                )

            messages.success(request, "Schedule updated successfully!")
            return redirect("view_schedule")
    else:
        form = ScheduleUploadForm()

    return render(request, "upload_page.html", {"form": form})

def view_schedule(request):
    # Path to your Excel file
    excel_path = "media/schedule.xlsx"

    try:
        df = pd.read_excel(excel_path)
        # Convert dataframe rows to a list of dictionaries
        schedule = df.to_dict(orient="records")
    except FileNotFoundError:
        schedule = []  # Empty list if file does not exist
    except Exception as e:
        schedule = []
        print("Error reading Excel file:", e)

    return render(request, "sports_app/view_schedule.html", {"schedule": schedule})


def result(request):
    return render(request, 'result.html')

def update_sports_score(request):
    return render(request, 'update_sports_score.html')




