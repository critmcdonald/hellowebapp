from django.shortcuts import render
from collection.models import Winery

# Create your views here.
def index(request):
    # defining the variable
    wineries = Winery.objects.all()
    # passing the variable to the view
    return render (request, 'index.html', {
        'wineries': wineries,
    })
