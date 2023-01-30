"""
Models for the GTDJ app. An app that tries to ease the use of the Getting Things Done methodology.
"""

from django.db import models


class Item(models.Model):
    """
    A model for an item in the GTDJ app.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class InBasketItem(Item):
    """
    A model for an item in the in-basket.
    """

    def __str__(self):
        return self.title


class NextActionItem(Item):
    """
    A model for an item in the next action list.
    """

    def __str__(self):
        return self.title


class ProjectItem(Item):
    """
    A model for an item in the project list.
    """

    next_action = models.ForeignKey(
        NextActionItem, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Contact information for a person or organization.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class WaitingForItem(Item):
    """
    A model for an item in the waiting for list.
    """

    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class SomedayMaybeItem(Item):
    """
    A model for an item in the someday/maybe list.
    """

    def __str__(self):
        return self.title


class ReferenceItem(Item):
    """
    A model for an item in the reference list.
    """

    def __str__(self):
        return self.title


class CalendarItem(Item):
    """
    A model for an item in the calendar.
    """

    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class TicklerItem(Item):
    """
    A model for an item in the tickler file.
    """

    date = models.DateTimeField()

    def __str__(self):
        return self.title


class TrashItem(Item):
    """
    A model for an item in the trash.
    """

    trashed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
