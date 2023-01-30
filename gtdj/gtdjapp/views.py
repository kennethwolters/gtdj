from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from gtdjapp.models import InBasketItem, NextActionItem, ProjectItem, WaitingForItem, Contact, TicklerItem

class InBasketItemListView(ListView):
    """Generic class-based view for a list of in_basket_items."""
    model = InBasketItem
    template_name = 'in_basket_item_list.html'
    context_object_name = 'in_basket_items'

class InBasketItemDetailView(DetailView):
    """Generic class-based detail view for an in_basket_item."""
    model = InBasketItem
    template_name = 'in_basket_item_detail.html'
    context_object_name = 'in_basket_item'

class InBasketItemCreateView(CreateView):
    """Generic class-based view for creating an in_basket_item."""
    model = InBasketItem
    template_name = 'in_basket_item_new.html'
    fields = ['title', 'description']
    success_url = '/in_basket_items/'

class InBasketItemUpdateView(UpdateView):
    """Generic class-based view for updating an in_basket_item."""
    model = InBasketItem
    template_name = 'in_basket_item_edit.html'
    fields = ['title', 'description', 'project', 'contact', 'tickler_date']
    success_url = '/in_basket_items/'

class InBasketItemDeleteView(DeleteView):
    """Generic class-based view for deleting an in_basket_item."""
    model = InBasketItem
    template_name = 'in_basket_item_delete.html'
    success_url = '/in_basket_items/'

