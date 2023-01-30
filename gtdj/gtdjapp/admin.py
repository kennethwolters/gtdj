from django.contrib import admin
from .models import InBasketItem, NextActionItem, ProjectItem, WaitingForItem, Contact, TicklerItem

admin.site.register(InBasketItem)
admin.site.register(NextActionItem)
admin.site.register(ProjectItem)
admin.site.register(WaitingForItem)
admin.site.register(Contact)
admin.site.register(TicklerItem)
