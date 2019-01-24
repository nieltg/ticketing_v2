from rest_framework import serializers

from .models import Ticket, TicketPurchase


class TicketPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPurchase
        fields = (
            'name',
            'email',
            'phone',
        )


class RedeemRequestSerializer(serializers.Serializer):
    ticket = serializers.SlugRelatedField(
        slug_field='code', queryset=Ticket.objects.all())


class RedeemPurchaseRequestSerializer(RedeemRequestSerializer):
    ticket_purchase = TicketPurchaseSerializer()


class RedeemResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPurchase
        fields = ('name', )
