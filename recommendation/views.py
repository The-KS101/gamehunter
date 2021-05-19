from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import gameSearched
from . import GetSimilar
from .models import Games
import re


# Create your views here.
def index(request):
    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            return redirect('similar_games', game, 'all')
        else:
            pass
    else:
        form = gameSearched()
        

    content = {
        'form': form,
        'games' : Games.objects.values_list('name', flat=True).distinct().order_by('name'),

    }
    return render(request, 'index.html', content)

def simGamesJson(request, game, console):
    console = None if console == 'all' else console
    similarGames, gameShown = GetSimilar.getRecommend(game, console=console)
    gameDets = []
    platforms = []
    for i in similarGames:
        if i != gameShown.lower():
            if console:
                gameDets.append(Games.objects.values().get(name__iexact=i, platform=console))
                platforms.append([console])
            else:
                gameDets.append(Games.objects.values().filter(name__iexact=i)[0])
                platforms.append([j.platform for j in Games.objects.filter(name__iexact=i)])
    

    imgNames = [prep(i['name']) for i in gameDets]
    return JsonResponse({'gameDets': gameDets, 'platforms': platforms, 'imgNames': imgNames,}, safe=False)


def simGames(request,  game, console):
    gameDets = ['as']
    gameShown = game
    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            platform = form.cleaned_data['platforms']
            sortBy = form.cleaned_data['sortOpt']
            ordChoice = form.cleaned_data['ordChoice']
            if sortBy:
                return redirect('similar_games_sorted', game, platform, sortBy, ordChoice)
            else:
                return redirect('similar_games', game, platform)
        else:
            print(form.errors)
    else:
        form = gameSearched()

    content = {
        'form': form,
        'games' : Games.objects.values_list('name', flat=True).distinct().order_by('name'),
        'gameDets': gameDets,
        'gameShowing': gameShown,
        'console': console,
    }
    
    return render(request, 'similar_games.html', content)


def simGamesSorted(request, game, console, sortBy, ordChoice):
    console = None if console == 'all' else console
    similarGames, gameShown = GetSimilar.getRecommend(game, console=console, sort=sortBy, order=ordChoice)
    gameDets = []
    platforms = []
    
    for i in similarGames:
        if i != gameShown.lower():
            if console:
                gameDets.append(Games.objects.get(name__iexact=i, platform=console))
                platforms.append([console])
            else:
                gameDets.append(Games.objects.filter(name__iexact=i)[0])
                platforms.append([j.platform for j in Games.objects.filter(name__iexact=i)])
    
    gameDets = zip(gameDets, platforms)
    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            platform = form.cleaned_data['platforms']
            sortBy = form.cleaned_data['sortOpt']
            ordChoice = form.cleaned_data['ordChoice']

            if sortBy:
                return redirect('similar_games_sorted', game, platform, sortBy, ordChoice)
            else:
                return redirect('similar_games', game, platform)
        else:
            print(form.errors)
    else:
        form = gameSearched()

    content = {
        'form': form,
        'games' : Games.objects.values_list('name', flat=True).distinct().order_by('name'),
        'gameDets': gameDets,
        'gameShowing': gameShown,
    }
    
    return render(request, 'similar_games.html', content)



def prep(a):
    a = re.sub('[^A-Za-z0-9 ]+', '', a)
    # a = re.sub(' ', '+', a)
    a += '.jpg'
    return a