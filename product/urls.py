from django.urls import path, include
from django.conf import settings
from .views import home,detail
app_name="product"
urlpatterns = [
    path("",home,name="home"),
    path("product/<int:product_id>/",detail,name='detail'),
]

