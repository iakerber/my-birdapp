from django.shortcuts import render

# Create your views here.
def waterbird_list(request):
    return render(request, 'birdid/waterbird_list.html', {})