import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from .models import *
from django.http import JsonResponse
from payments.models import Price
from payments.models import *

from django.views.generic.base import TemplateView
import json



# stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

print(stripe.api_key,'--------------stripe')

class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        print(self.kwargs["pk"],'================pkkkk')
        price = Price.objects.get(id=self.kwargs["pk"])
 
        price3 = Price.objects.get(id=3)
        print('price------',price)
        print('price.stripe_price_id-------',price.stripe_price_id)
        # print('^^^^^^^^^^^^^^^^^^^^^^^^^',settings.BASE_URL)
        product_id = kwargs.get("pk")
        print('price------',price)
        print('price.stripe_price_id-------',price.stripe_price_id)
        # print('^^^^^^^^^^^^^^^^^^^^^^^^^',settings.BASE_URL)
        product_id = kwargs.get("pk")
        print(settings.BASE_URL,'===============settings.BASE_URL')
        # product = Product.objects.get(id=product_id)
        checkout_session = stripe.checkout.Session.create(
            # payment_method_types=['card'],
            line_items=[
                {
                    "price" : price.stripe_price_id,
                    "quantity": 2,
                },         
                {
                    "price" : price3.stripe_price_id,
                    "quantity": 10,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL + '/payments/success/',
            cancel_url=settings.BASE_URL + '/payments/cancel/',
        )
 
        print(checkout_session,'=============checkout_session')
        return redirect(checkout_session.url)

class SuccessView(TemplateView):
    template_name = "payments/success.html"


class CancelView(TemplateView):
    template_name = "payments/cancel.html"