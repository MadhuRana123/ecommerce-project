from django.urls import path
from app import views

from payments.views import CancelView, SuccessView, CreateCheckoutSessionView

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
