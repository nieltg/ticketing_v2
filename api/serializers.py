from rest_framework import serializers

from .models import Ticket, TicketPurchase


class RedeemRequestSerializer(serializers.Serializer):
    ticket = serializers.SlugRelatedField(
        slug_field='code', queryset=Ticket.objects.all())


class RedeemResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPurchase
        fields = ('name', )
