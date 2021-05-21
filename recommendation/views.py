from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import gameSearched
from . import GetSimilar
from .models import Games
import re


# Create your views here.
def gameListJson(request):
    games = Games.objects.values_list('name', flat=True).distinct().order_by('name')
    return JsonResponse(list(games), safe=False)

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
                try:
                    gameDets.append(Games.objects.values().filter(name__iexact=i)[0])
                    platforms.append([j.platform for j in Games.objects.filter(name__iexact=i)])
                except:
                    i = re.sub('/', '', i)
                    pass
    

    imgNames = [prep(i['name']) for i in gameDets]
    return JsonResponse({'gameDets': gameDets, 'platforms': platforms, 'imgNames': imgNames,}, safe=False)

def featured_games(request):
    featured = Games.objects.values().filter(featured=True)
    imgNames = [prep(i['name']) for i in featured]

    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            platform = form.cleaned_data['platforms']
            return redirect('similar_games', game, platform)
        else:
            print(form.errors)
    else:
        form = gameSearched()

    content = {
        'form': form,
        'featured': featured,
        'imgs': imgNames,
    }

    return render(request, "featured_games.html", content)

def about(request):
    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            platform = form.cleaned_data['platforms']
            return redirect('similar_games', game, platform)
        else:
            print(form.errors)
    else:
        form = gameSearched()

    content = {
        'form': form,
    }
    return render(request, 'about.html', content)

def simGames(request,  game, console):
    gameShown = game
    if request.method == "GET":
        form = gameSearched(request.GET)
        if form.is_valid():
            game = form.cleaned_data['gameName']
            platform = form.cleaned_data['platforms']
            return redirect('similar_games', game, platform)
        else:
            print(form.errors)
    else:
        form = gameSearched()

    content = {
        'form': form,
        'gameShowing': gameShown,
        'console': console,
    }
    
    return render(request, 'similar_games.html', content)


def prep(a):
    a = re.sub('[^A-Za-z0-9 ]+', '', a)
    a += '.jpg'
    return a