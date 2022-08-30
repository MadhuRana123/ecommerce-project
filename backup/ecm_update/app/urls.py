from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MypasswordResetForm
# from .views import StripeIntentView, custom_payment_view

urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailview.as_view(), name='product-detail'),
    path('cart/',views.show_cart,name ='showcart'),
    path('update-qty/',views.update_qty,name ='update_qty'),
    path('remove-cart/',views.remove_cart,name ='remove_cart'),
    path('cart/<str:product_id>',views.add_show_Cart,name='add_show_Cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    # path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),
    # path('paymentdone/', views.payment_done, name='paymentdone'),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm,next_page='profile'),name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",
    form_class=MyPasswordChangeForm), name='passwordchange'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MypasswordResetForm),name='password_reset'),
    path('orders/', views.orders, name='orders'),
    path('success/', views.success, name='success'), # new    

    # path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    # path('custom-payment/', CustomPaymentView.as_view(), name='custom-payment')
  
]   
