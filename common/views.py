from django.shortcuts import render

# Create your views here.

def index(request):
    # TODO: display login info for logged in users somewhere
    return render(request, "common/homepage.html")
