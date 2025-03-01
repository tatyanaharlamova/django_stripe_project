from django.views.generic import DetailView

from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import stripe
from django.conf import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request, id, *args, **kwargs):
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return JsonResponse({'session_id': session.id})


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
