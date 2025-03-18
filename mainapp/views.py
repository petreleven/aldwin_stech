from tokenize import Single
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Player
from .models import Movie

# Create your views here.
def homepage( request ):
    return HttpResponse("hello from python")

def loginpage( request ):
    #return HttpResponse(" <input> ")
    print("You did a"+ request.method)
    if request.method == "POST":
        print( request.POST)
        typedname = request.POST.get("Username")
        print("The name you typed is :" + typedname)
        typedPassword = request.POST.get("Password")
        print(typedPassword)
        new_Player =Player(username = typedname, password = typedPassword)  
        new_Player.save()  
    return render(request, "login.html")

def moviepage( request ):
    print("You did a"+ request.method)
    if request.method == "POST":
        print( request.POST)
        moviename = request.POST.get("name")
        print("The name you typed is :" + moviename)
        MovieDescription = request.POST.get("description")
        print(MovieDescription)
        new_Movie =Movie(Name= moviename, Description = MovieDescription)  
        new_Movie.save()
    return render(request, "movie.html")

def fetch_all_players_page(request):
    all_players = Player.objects.all()
    return render(request, "all_players.html", {"all_player": all_players})

def fetch_all_movies_page(request):
    all_movies = Movie.objects.all() # type: ignore
    return render(request, "movies.html", {"all_movies": all_movies})

def fetch_one_player_page(request, pk):
    single_player = Player.objects.get(pk = pk)
    return render(request, "oneplayer.html", {"single_player": single_player})

def fetch_one_movie_page(request, pk):
    single_movie = Movie.objects.get(pk = pk)
    return render(request, "onemovie.html", {"single_movie": single_movie})

def update_one_player(request, pk):
    single_player = Player.objects.get(pk=pk)
    if request.method == "POST":
        new_username = request.POST.get("username")
        new_password = request.POST.get("password")
        single_player.username = new_username
        single_player.password = new_password
        single_player.save()
    return render(request,
                  "update_one_player.html",
                  {"single_player":single_player})

def update_one_movie(request, pk):
    single_movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        new_Name = request.POST.get("Name")
        new_Description = request.POST.get("Description")
        single_movie.Name = new_Name
        single_movie.Description = new_Description
        single_movie.save()
    return render(request,
                  "update_one_movie.html",
                  {"single_movie":single_movie})

def delete_one_player(request, pk):
    single_player = Player.objects.get(pk=pk)
    single_player.delete()
    return redirect("homepage")
