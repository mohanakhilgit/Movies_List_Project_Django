from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import Movie
from .forms import MovieForm

# Create your views here.


def home(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        description = request.POST.get('desc')
        img = request.FILES['image']

        movie = Movie(name=name, year=year, description=description, img=img)
        movie.save()
        return redirect('')
    return render(request, 'add.html')


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'delete.html', {'movie': movie})
