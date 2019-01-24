from django.urls import include, path

from .views import redeem, redeem_purchase

urlpatterns = [
    path('redeem/', redeem, name='redeem'),
    path('redeem-purchase/', redeem_purchase, name='redeem-purchase'),
]
