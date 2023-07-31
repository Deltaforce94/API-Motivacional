from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.motivation_quote_list, name='quote-list'),
    path('quotes/random/', views.random_motivation_quote, name='random-quote'),
]
