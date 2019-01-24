from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import set_rollback

from .models import SouvenirRedeem, Ticket, TicketPurchase
from .serializers import RedeemRequestSerializer, RedeemResponseSerializer


@api_view(['POST'])
def redeem(request: Request) -> Response:
    serializer = RedeemRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    ticket = serializer.validated_data['ticket']

    try:
        ticket_purchase = ticket.ticket_purchase
    except ObjectDoesNotExist:
        raise exceptions.APIException(
            "Ticket has not purchased yet", code="ticket_not_purchased")

    try:
        _ = ticket_purchase.souvenir_redeem

        raise exceptions.APIException(
            "Souvenir has been redeemed", code="souvenir_redeemed")
    except ObjectDoesNotExist:
        pass

    souvenir_redeem = SouvenirRedeem(ticket_purchase=ticket_purchase)
    souvenir_redeem.save()

    out = RedeemResponseSerializer(ticket_purchase)
    return Response(out.data)


@api_view(['POST'])
def redeem_purchase(request: Request) -> Response:
    pass


def exception_handler(exc, context):
    #pylint: disable=unused-argument

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        data = exc.get_full_details()

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None
