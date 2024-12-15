from django.shortcuts import render, get_object_or_404, redirect
from .models import Waterbird
from .forms import WaterbirdForm
from .models import Raptor, Songbird
from .forms import RaptorForm, SongbirdForm

# Create your views here. Waterbird views
def mainpage(request):
    return render(request, 'birdid/mainpage.html')

def waterbird_list(request):
    waterbirds = Waterbird.objects.all()
    return render(request, 'birdid/waterbird_list.html', {'waterbirds': waterbirds})

def waterbird_detail(request, pk):
    waterbird = get_object_or_404(Waterbird, pk=pk)
    return render(request, 'birdid/waterbird_detail.html', {'waterbird': waterbird})

def waterbird_new(request):
    if request.method == "POST":
        form = WaterbirdForm(request.POST)
        if form.is_valid():
            waterbird = form.save()
            waterbird.save()
            return redirect('waterbird_detail', pk=waterbird.pk)
    else:
        form = WaterbirdForm()
    return render(request, 'birdid/waterbird_edit.html', {'form': form})

def waterbird_edit(request, pk):
    waterbird = get_object_or_404(Waterbird, pk=pk)
    if request.method == "POST":
        form = WaterbirdForm(request.POST, instance=waterbird)
        if form.is_valid():
            waterbird = form.save()
            waterbird.save()
            return redirect('waterbird_detail', pk=waterbird.pk)
    else:
        form = WaterbirdForm(instance=waterbird)
    return render(request, 'birdid/waterbird_edit.html', {'form': form})

#raptor views
def raptor_list(request):
    raptors = Raptor.objects.all()
    return render(request, 'birdid/raptor_list.html', {'raptors': raptors})

def raptor_detail(request, pk):
    raptor = get_object_or_404(Raptor, pk=pk)
    return render(request, 'birdid/raptor_detail.html', {'raptor': raptor})

def raptor_new(request):
    if request.method == "POST":
        form = RaptorForm(request.POST, request.FILES)
        if form.is_valid():
            raptor = form.save()
            raptor.save()
            return redirect('raptor_detail', pk=raptor.pk)
    else:
        form = RaptorForm()
    return render(request, 'birdid/raptor_edit.html', {'form': form})

def raptor_edit(request, pk):
    raptor = get_object_or_404(Raptor, pk=pk)
    if request.method == "POST":
        form = RaptorForm(request.POST, instance=raptor)
        if form.is_valid():
            raptor = form.save()
            raptor.save()
            return redirect('raptor_detail', pk=raptor.pk)
    else:
        form = RaptorForm(instance=raptor)
    return render(request, 'birdid/raptor_edit.html', {'form': form})


    #songbird views
def songbird_list(request):
    songbirds = Songbird.objects.all()
    return render(request, 'birdid/songbird_list.html', {'songbirds': songbirds})

def songbird_detail(request, pk):
    songbird = get_object_or_404(Songbird, pk=pk)
    return render(request, 'birdid/songbird_detail.html', {'songbird': songbird})

def songbird_new(request):
    if request.method == "POST":
        form = SongbirdForm(request.POST, request.FILES)
        if form.is_valid():
            songbird = form.save()
            songbird.save()
            return redirect('songbird_detail', pk=songbird.pk)
    else:
        form = SongbirdForm()
    return render(request, 'birdid/songbird_edit.html', {'form': form})

def songbird_edit(request, pk):
    songbird = get_object_or_404(Songbird, pk=pk)
    if request.method == "POST":
        form = SongbirdForm(request.POST, instance=songbird)
        if form.is_valid():
            songbird = form.save()
            songbird.save()
            return redirect('songbird_detail', pk=songbird.pk)
    else:
        form = SongbirdForm(instance=songbird)
    return render(request, 'birdid/songbird_edit.html', {'form': form})