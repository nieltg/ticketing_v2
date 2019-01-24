from django.db import models


class Ticket(models.Model):
    code = models.CharField(
        max_length=13, blank=False, null=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TicketPurchase(models.Model):
    ticket = models.OneToOneField(
        Ticket, on_delete=models.PROTECT, primary_key=True)

    name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SouvenirRedeem(models.Model):
    ticket_purchase = models.OneToOneField(
        TicketPurchase, on_delete=models.PROTECT, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
