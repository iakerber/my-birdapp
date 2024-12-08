from django.shortcuts import render, get_object_or_404
from .models import Waterbird

# Create your views here.
def waterbird_list(request):
    waterbirds = Waterbird.objects.all()
    return render(request, 'birdid/waterbird_list.html', {'waterbirds': waterbirds})

def waterbird_detail(request, pk):
    waterbird = get_object_or_404(Waterbird, pk=pk)
    return render(request, 'birdid/waterbird_detail.html', {'waterbird': waterbird})