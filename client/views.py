from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'client/index.html')

def about(request):
    return render(request, 'client/about.html')

def contact(request):
    return render(request, 'client/contact.html')

def faq(request):
    return render(request, 'client/faq.html')

def overview(request):
    return render(request, 'client/dashboard/overview.html')

def bet_history(request):
    return render(request, 'client/dashboard/bet_history.html')

def transaction_history(request):
    return render(request, 'client/dashboard/transaction_history.html')

def deposit(request):
    return render(request, 'client/dashboard/deposit.html')

def withdraw(request):
    return render(request, 'client/dashboard/withdraw.html')

def refferal(request):
    return render(request, 'client/dashboard/refferal.html')

def settings(request):
    return render(request, 'client/dashboard/settings.html')

