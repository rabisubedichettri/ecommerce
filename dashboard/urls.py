from django.urls import path, include
from .views import dashboard_view
from product.views import (product_category,product_create,
                    add_product_images,product_offer,product_category_publish,product_category_log)

app_name="dashboard"
urlpatterns = [
    path('product/category/',product_category,name="product-category"),



    path('',dashboard_view,name="view"),
    path('product/category/view',product_category,name="product-category-view"),
     path('product/category/publish',product_category_publish,name="product-category-publish"),
     path('product/category/log',product_category_log,name="product-category-log"),
     
    path('product/category/add',product_category,name="product-category-add"),
    path('product/create/',product_create,name="product-create"),
    path('product/<int:product_id>/images/add',add_product_images,name="add-product-images"),


    path("product/offer/",product_offer,name="product_offer"),

]
