from django.db.models import Count
from django.shortcuts import render

# Create your views here.
import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.template import Context

from .models import Task
from django.http import HttpResponse, JsonResponse
from collections import Counter
import  pandas as pd
# Create your views here.
# one parameter named request
from sqlalchemy import create_engine
from django.views.generic import View
from .models import Task
import psycopg2
import json


def profile_upload(request):

        # declaring template
        template = "profile_upload.html"
        # data = Profile.objects.all()
        # prompt is a context variable that can have different values      depending on their context
        prompt = {
            'order': 'Order of the CSV should be id, season, city, date, team1',
            # 'profiles': data
                  }
        # GET request returns the value of the data with the specified key.
        if request.method == "GET":
            return render(request, template, prompt)
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if  csv_file.name.endswith('.csv'):
            # messages.error(request,'THIS IS NOT A CSV FILE')
        # data_set = csv_file.read().decode('UTF-8')
            data_set=pd.read_csv(csv_file)
            engine = create_engine('postgresql://postgres:Mahesh1990@localhost:5432/Task')
            data_set.to_sql('ipl_matches_task', engine,if_exists='replace')

            context = {}
            return render(request, template, context)
        else:
            return HttpResponse(json.dumps({"Note":"Please enter a valid csv file"}))



def home(request):
    return render(request, 'home.html')


def population_chart(request):
    labels = []
    data = []

    queryset = Task.objects.values()[:5]
    for entry in queryset:
        labels.append(entry['winner'])
        data.append(entry['win_by_runs'])


    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []
    output=[]
    count=0
    # queryset = profile_data.objects.values()[:5]

    queryset = Task.objects.values()[:5]

    for city in queryset:
        labels.append(city["winner"])
        data.append(city["win_by_runs"])


    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,

    })

def maximum_player_match(request):
    players=[]
    players_list=[]
    labels=[]
    data=[]
    # queryset = profile_data.objects.values()[:5]

    queryset = Task.objects.values("player_of_match")

    for city in queryset:
        players.append(city)
    for j in players:
        players_list.append(j["player_of_match"])
    output={k: v for k, v in sorted(Counter(players_list).items(), key=lambda item: item[1])}
    return JsonResponse({
        'player won maximum number of player of the match': list(output.keys())[-1],
        'no of times player won':list(output.values())[-1]

    })

def toss_winner(request):
    players=[]
    players_list=[]

    # queryset = profile_data.objects.values()[:5]

    queryset = Task.objects.values("toss_winner")

    for city in queryset:
        players.append(city)
    for j in players:
        players_list.append(j["toss_winner"])


    return JsonResponse({
        'toss_winner': list(Counter(players_list).keys())[0],
        'no of times winner won the toss':list(Counter(players_list).values())[0]

    })

def winner(request):
    players=[]
    players_list=[]

    # queryset = profile_data.objects.values()[:5]

    queryset = Task.objects.values("winner")

    for city in queryset:
        players.append(city)
    for j in players:
        players_list.append(j["winner"])


    return JsonResponse({
        'winner':list(Counter(players_list).keys())[0],
        'no of times won':list(Counter(players_list).values())[0]

    })

# Create your views here.
