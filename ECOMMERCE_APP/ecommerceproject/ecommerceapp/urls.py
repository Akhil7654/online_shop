from . import views
from django.urls import path

app_name='ecommerceapp'

urlpatterns = [
    path('',views.allproducts,name='allproducts'),
    path('<slug:cslug>/',views.allproducts,name='products_category'),
    path('<slug:cslug>/<slug:product_slug>/',views.prodetail,name='product_category_detail')
]


