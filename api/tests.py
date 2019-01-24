from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from .factories import (SouvenirRedeemFactory, TicketFactory,
                        TicketPurchaseFactory)
from .models import SouvenirRedeem, Ticket, TicketPurchase
from .serializers import RedeemResponseSerializer


class EmptyRedeemViewTest(APITestCase):
    client = APIClient()

    def test_redeem_no_object(self):
        response = self.client.post(
            reverse('redeem'), data={'ticket': "1234567890000"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TicketRedeemTest(APITestCase):
    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.data_ticket = TicketFactory()

    def test_redeem_no_purchase(self):
        response = self.client.post(
            reverse('redeem'), data={'ticket': self.data_ticket.code})

        self.assertEqual(response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['code'], 'ticket_not_purchased')


class TicketPurchaseRedeemTest(APITestCase):
    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.data_ticket_purchase = TicketPurchaseFactory()

    def test_redeem_no_redeem(self):
        response = self.client.post(
            reverse('redeem'),
            data={'ticket': self.data_ticket_purchase.ticket.code})

        expected = RedeemResponseSerializer(self.data_ticket_purchase)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)


class SouvenirRedeemRedeemTest(APITestCase):
    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.data_souvenir_redeem = SouvenirRedeemFactory()

    def test_redeem_redeemed(self):
        ticket_purchase = self.data_souvenir_redeem.ticket_purchase

        response = self.client.post(
            reverse('redeem'), data={'ticket': ticket_purchase.ticket.code})

        self.assertEqual(response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['code'], 'souvenir_redeemed')
