from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Account
import csv

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
            information = Account(account_text=data, account_money=money, pub_date=date)
            information.save()
    # user hits the Back button.
    return render(request,"account/detail.html",'')

def history(request):
    payment_list = Account.objects.order_by('-pub_date')
    total = 0
    for money in payment_list:
        total = total + money.account_money
    # Calculate balance of paylist.
    return render(request,"account/history.html",{'payment_list':payment_list, 'amt_total':total})

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['data', 'value', 'date'])
    payment_list = Account.objects.order_by('-pub_date')
    for money in payment_list:
        writer.writerow([money.account_text, money.account_money, money.pub_date])

    return response
