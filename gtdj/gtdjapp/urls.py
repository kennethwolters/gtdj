from django.urls import path
from . import views

urlpatterns = [
    path('', views.InBasketItemListView.as_view(), name='in_basket_item_list'),
    path('<int:pk>/', views.InBasketItemDetailView.as_view(), name='in_basket_item_detail'),
    path('new/', views.InBasketItemCreateView.as_view(), name='in_basket_item_new'),
    path('<int:pk>/edit/', views.InBasketItemUpdateView.as_view(), name='in_basket_item_edit'),
    path('<int:pk>/delete/', views.InBasketItemDeleteView.as_view(), name='in_basket_item_delete'),
]