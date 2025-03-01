from store.apps import StoreConfig
from django.urls import path
from .views import BuyItemView, ItemDetailView

app_name = StoreConfig.name

urlpatterns = [
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy_item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]