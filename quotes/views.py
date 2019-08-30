from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
import requests
import json


def home(request):
    if request.method == "POST":
        ticker = request.POST['ticker']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_f531f0627f2247ae9f1cf13f043ba8a2")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request, 'home.html', {"api": api})
    else:
        return render(request, 'home.html', {"ticker": "Enter A Valid Stock Code Above"})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock Added To Portfolio")
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for x in ticker:
            x = str(x)
            api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{x}/quote?token=pk_f531f0627f2247ae9f1cf13f043ba8a2")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error"
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})



def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Item Deleted Successfully"))
    return redirect(delete_stock)


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})