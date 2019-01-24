import string

from factory import DjangoModelFactory, SubFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyText

from .models import SouvenirRedeem, Ticket, TicketPurchase


class TicketFactory(DjangoModelFactory):
    code = FuzzyText(length=13, chars=string.digits)

    class Meta:
        model = Ticket


class TicketPurchaseFactory(DjangoModelFactory):
    name = Faker("name")
    email = Faker("email")
    phone = Faker("phone_number")

    ticket = SubFactory(TicketFactory)

    class Meta:
        model = TicketPurchase


class SouvenirRedeemFactory(DjangoModelFactory):
    ticket_purchase = SubFactory(TicketPurchaseFactory)

    class Meta:
        model = SouvenirRedeem
