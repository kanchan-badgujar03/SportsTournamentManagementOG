
from django.db import models

class FootballGame(models.Model):
    Team_1_Name=models.CharField(max_length=50)
    Team_2_Name=models.CharField(max_length=50)
    Match_Date=models.DateField()
    Match_Time=models.TimeField()
    Location=models.CharField(max_length=100)
    Final_Score=models.CharField(max_length=20, blank=True, null=True)
    Remarks=models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.Team_1_Name} vs {self.Team_2_Name} - {self.Match_Date}"
    
class BasketballGame(models.Model):
    Team_1_Name=models.CharField(max_length=50)
    Team_2_Name=models.CharField(max_length=50)
    Match_Date=models.DateField()
    Match_Time=models.TimeField()
    Location=models.CharField(max_length=100)
    Final_Score=models.CharField(max_length=20, blank=True, null=True)
    Remarks=models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.Team_1_Name} vs {self.Team_2_Name} - {self.Match_Date}"
    
class NewTeam(models.Model):
    Team_Name = models.CharField(max_length=100)
    Sport = models.CharField(max_length=50, choices=[
        ("Football", "Football"),
        ("Cricket", "Cricket"),
        ("Basketball", "Basketball"),
        ("Volleyball", "Volleyball"),
    ])
    Coach_Name = models.CharField(max_length=100)
    Number_of_Players = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Team_Name} ({self.Sport})"
    

class NewGame(models.Model):
    New_Game = models.CharField(max_length=100)
    Indoor_Outdoor = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.New_Game} ({self.Indoor_Outdoor})"

class Sport(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # Indoor/Outdoor/etc.
    description = models.TextField(blank=True)

    def __str__(self):

        """
        Return a string representation of the sport.

        :return: A string containing the sport's name.
        :rtype: str
        """

        return self.name

class Event(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.sport.name}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    sport =  models.ForeignKey(Sport, on_delete=models.CASCADE)
    coach = models.CharField(max_length=100, blank=True, null=True)
    players_count=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Score(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='scores')
    team_name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.event.name} - {self.team_name} ({self.points})"
    
class MatchSchedule(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_date = models.DateField()
    match_time = models.TimeField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.match_date}"
    

