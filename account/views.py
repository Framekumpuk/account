from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Data

def index(request):
    return render(request,"account/index.html",'')
    
def operand(request):
    error_message = 0 
    try:
        paylist = request.POST['paylist']
        data = request.POST['data']
        money = request.POST['value']
        date = request.POST['date']
        if paylist != 'income':
            money = int(money)*-1
    except:
        error_message = 1
        data = ""
        money = ""
        date = ""
    else:
            information = Data(data_text=data, data_money=money, pub_date=date)
            information.save()
    return render(request,"account/detail.html",'')

def history(request):
    payment_list = Data.objects.order_by('-pub_date')
    total = 0
    for money in payment_list:
        total = total + money.data_money
    return render(request,"account/history.html",{'payment_list':payment_list, 'amt_total':total})
