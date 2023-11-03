from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'menus/index.html')
    # return HttpResponse('<h1>Menus Index...</h1>')