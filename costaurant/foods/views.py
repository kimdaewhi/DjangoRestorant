from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.today().date()
    print(today)
    context = {"date": today}
    
    # 3번째 파라미터에 context 추가하여 전달
    return render(request, 'foods/index.html', context=context)



def food_detail(request, food): 
    context = dict()
    
    if food == "karaage":
        context["name"] = "가라아게"
        context["desc"] = "튀김이 얇고 바삭한 일본식 닭튀김 요리"
        context["price"] = 14000
        context["img_path"] = "foods/images/karaage.jpg"
    else:
        raise Http404("이런 음식은 없다구요!")
    
    return render(request, 'foods/detail.html', context=context)