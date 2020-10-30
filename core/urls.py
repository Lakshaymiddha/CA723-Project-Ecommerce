from django.urls import path
from .views import item_list

app_name = 'core'

urlpatterns = [
    path('/list',item_list,name = 'item_list'),
    path('', HomeView.as_view(), name='home'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
]

