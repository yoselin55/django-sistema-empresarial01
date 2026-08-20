from django.urls import path
from .views import item_list, api_items, api_demo

urlpatterns = [
    path('', item_list, name='item_list'),
    path('api/items/', api_items, name='api_items'),
    path('api-demo/', api_demo, name='api_demo'),
]