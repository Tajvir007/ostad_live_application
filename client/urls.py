from django.urls import path
from . import views

app_name = "client"

urlpatterns = [
    path('', views.index, name="index"),

    path('user/overview/', views.overview, name="overview"),
    path('user/bet-history/', views.bet_history, name="bet_history"),
    path('user/transaction-history/', views.transaction_history, name="transaction_history"),
    path('user/deposit/', views.deposit, name="deposit"),
    path('user/withdraw/', views.withdraw, name="withdraw"),
    path('user/referral/', views.refferal, name="refferal"),
    path('user/settings/', views.settings, name="settings"),

    path('about-us/', views.about, name="about-us"),
    path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name="faq")

]
