from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import SouvenirRedeem, Ticket, TicketPurchase

@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    pass

@admin.register(TicketPurchase)
class TicketPurchaseAdmin(ImportExportModelAdmin):
    pass

admin.site.register(SouvenirRedeem)
