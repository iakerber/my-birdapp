from django.shortcuts import render
from .models import Waterbird

# Create your views here.
def waterbird_list(request):
    waterbirds = Waterbird.objects.all()
    return render(request, 'birdid/waterbird_list.html', {'waterbirds': waterbirds})