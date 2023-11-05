from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = dict()
    
    menus = Menu.objects.all()
    
    context["date"] = today
    context["menus"] = menus
    
    # 3번째 파라미터에 context 추가하여 전달
    return render(request, 'foods/index.html', context=context)



def food_detail(request, pk): 
    context = dict()
    
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    
    # raise Http404("이런 음식은 없다구요!")
    return render(request, 'foods/detail.html', context=context)