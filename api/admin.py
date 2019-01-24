from django.contrib import admin

from .models import SouvenirRedeem, Ticket, TicketPurchase

admin.site.register(Ticket)
admin.site.register(TicketPurchase)
admin.site.register(SouvenirRedeem)
