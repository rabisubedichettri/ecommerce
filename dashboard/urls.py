from django.urls import path, include
from .views import dashboard_view
from product.views import (product_category,product_create,
                    add_product_images,product_offer)

app_name="dashboard"
urlpatterns = [
    path('product/category/',product_category,name="product-category"),



    path('',dashboard_view,name="view"),
    path('product-category/',product_category,name="product-category"),
    path('product/create/',product_create,name="product-create"),
    path('product/<int:product_id>/images/add',add_product_images,name="add-product-images"),


    path("product/offer/",product_offer,name="product_offer"),

]
