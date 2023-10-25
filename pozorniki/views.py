from django.shortcuts import render
from .models import Pozorniki


# Create your views here.
def index(request):
    return render(request, 'index.html',
                  {'pozorniki': sorted(Pozorniki.objects.all(), key=lambda x: x.ochki_pozora)})