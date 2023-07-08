from django.urls import path     
from . import views

app_name = 'app'
urlpatterns = [
    # Page Section:
    path('', views.index, name='home'),
    path('registration', views.registration, name='registration'),
    path('products', views.products, name='products'),
    path('new_product_page', views.new_product_page, name='new_product_page'),                      


    # Process Section
    path('reg_process', views.reg_process, name='reg_process'),                      
    path('login_process', views.login_process, name='login_process'),                      
    path('logout_process', views.logout_process, name='logout_process'),                      
    path('new_product_process', views.new_product_process, name='new_product_process'),                      
    path('delete_product_process/<int:product_id>', views.delete_product_process, name='delete_product_process'),                      

]