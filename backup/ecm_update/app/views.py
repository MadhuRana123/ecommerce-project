
from ast import Add
# from audioop import add
from pickle import GET
from django.contrib import messages
from unicodedata import category
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from django.http import HttpResponse
from.forms import CustomerRegistrationForm,CustomerProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.conf import settings
from payments.models import *

from django.views.generic.base import TemplateView
import json
# import stripe

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        # print(topwears, '@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        bottomwears = Product.objects.filter(category='BM')
        # print(bottomwears, '==========')
        mobiles = Product.objects.filter(category='M')
        return render(request,'app/home.html',{'topwears':topwears, 
        'bottomwears':bottomwears,'mobiles':mobiles})




class ProductDetailview(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)      
        return render(request, 'app/productdetail.html', {'product':product})

def add_show_Cart(request,product_id=None):
    if request.user.is_authenticated:
        user = request.user      
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart,created = Cart.objects.get_or_create(user=user, product_id=product_id)
        if created:    
            cart.save()   
        tempamount =(cart.quantity * cart.product.discounted_price)
        amount += tempamount
        totalamount = amount + shipping_amount
        context = {'totalamount':totalamount,'amount':amount}    
        context['carts'] = cart        
        # messages.success(request, 'congratulation!! add to cart successfully')
        return render(request, 'app/addtocart.html',context)


def show_cart(request):   
    if request.user.is_authenticated:
        user = request.user      
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount =(p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
        context = {'totalamount':totalamount,'amount':amount,'cart_product':cart_product}
        return render(request, 'app/showcartitems.html',context)

@csrf_exempt
def update_qty(request):
 
    # user = request.user  
    status = ''
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        count = request.POST.get('count')
        cart = Cart.objects.filter(id = cart_id ).first()          
        amount = 0.0
        shipping_amount = 70.0
   
        tempamount =(cart.quantity * cart.product.discounted_price)
       
        totalamount = tempamount + cart.product.discounted_price
        print(totalamount)  


        if cart and count:
            cart.quantity  = int(count)
            cart.save()
            status = True   
            tempamount =(cart.quantity * cart.product.discounted_price)
            amount += tempamount
                
            totalamount = amount + shipping_amount    
           
        else:
            status = False
            tempamount =(cart.quantity * cart.product.discounted_price)
            amount += tempamount

            totalamount = amount + shipping_amount 
              
        data = {'status':status , 'totalamount': totalamount ,'amount':amount}        
        return JsonResponse(data)
    
    return render_to_string("app/addtocart.html")

@csrf_exempt
def remove_cart(request):
 
    # user = request.user  
    status = ''
    if request.method == 'POST':
        
        cart_id = request.POST.get('cart_id')

        count = request.POST.get('count')
        cart = Cart.objects.filter(id = cart_id ).first()
        test = cart.delete() 
        if test!=0:
           data = {'status':'success'}
        else:
            data = {'status':'fail'}
        # data = {'status':status , 'totalamount': totalamount ,'amount':amount}        
        return JsonResponse(data)
        print('delete here')         
        amount = 0.0
        shipping_amount = 70.0
   
        tempamount =(cart.quantity * cart.product.discounted_price)
       
        totalamount = tempamount + cart.product.discounted_price
        print(totalamount)  


        if cart and count:
            cart.quantity  = int(count)
            cart.delete()
            status = True   
            tempamount =(cart.quantity * cart.product.discounted_price)
            amount += tempamount
                
            totalamount = amount + shipping_amount    
           
        else:
            status = False
            tempamount =(cart.quantity * cart.product.discounted_price)
            amount += tempamount

            totalamount = amount + shipping_amount 
              
        data = {'status':status , 'totalamount': totalamount ,'amount':amount}        
        
    
    return render_to_string("app/addtocart.html")
                     
def buy_now(request):
    return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):   
    return render(request, 'app/orders.html')

def change_password(request):
  
    return render(request, 'app/passwordchange.html')

def mobile(request, data=None):
  
    if data == None:
        mobiles =  Product.objects.filter(category='M')
      
    elif data == 'Redmi' or data == 'Samsung':        
        mobiles =  Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Below':
        mobiles =  Product.objects.filter(category='M').filter( discounted_price__lte=10000)
    elif data == 'Above':
        mobiles =  Product.objects.filter(category='M').filter( discounted_price__gte=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})
  

def login(request):
 return render(request, 'app/login.html')

            
class CustomerRegistrationView(View):
    def get(self,request):
       form =CustomerRegistrationForm()
       #  print(form)
       return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
      
            messages.success(request, 'congratualtion!!  Registered successfully')
            form.save()
            return render(request, 'app/customerregistration.html',{'form':form})


def password_reset(request):
    return render(request, 'app/password_reset.html')


def checkout(request):
    user =request.user
    add= Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product =[p for p in Cart.objects.all()if p.user == request.user]
    if cart_product:
        for cart in cart_product:
            tempamount =(cart.quantity * cart.product.discounted_price)
            amount += tempamount
            totalamount = amount + shipping_amount
    key = settings.PUBLISHABLE_KEY
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items,'key': key})    

# def payment_done(request):
#     user = request.user
#     custid = request.GET.get('custid')   
#     customer = Customer.objects.get(id=custid)
#     cart = Cart.objects.filter(user=user)
#     for c in cart:
#         OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        # c.delete()
    #   retuen redirect("orders")
def success(request):
    return render(request,'app/success.html')
   
  

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form})

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        print(form)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'congratulation!! profile updated successfully')
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})

# class StripeIntentView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             req_json = json.loads(request.body)
#             customer = stripe.Customer.create(email=req_json['email'])
#             # price = Price.objects.get(id=self.kwargs["pk"])
#             intent = stripe.PaymentIntent.create(
#                 # amount=price.price,
#                 currency='usd',
#                 customer=customer['id'],
#                 metadata={
#                     # "price_id": price.id
#                 }
#             )
#             return JsonResponse({
#                 'clientSecret': intent['client_secret']
#             })
#         except Exception as e:
#             return JsonResponse({'error': str(e)})        

# class CustomPaymentView(TemplateView):
#     template_name = "custom_payment.html"

#     def get_context_data(self, **kwargs):
#         product = Product.objects.get(name="Test Product")
#         # prices = Price.objects.filter(product=product)
#         context = super(CustomPaymentView, self).get_context_data(**kwargs)
#         context.update({
#             "product": product,
#             # "prices": prices,
#             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
#         })
#         return context            