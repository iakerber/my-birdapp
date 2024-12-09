from django.shortcuts import render, get_object_or_404, redirect
from .models import Waterbird
from .forms import WaterbirdForm

# Create your views here.
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