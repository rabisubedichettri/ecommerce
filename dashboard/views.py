from django.shortcuts import render
from product.views import product_category

def dashboard_view(request):
    return render(request,"base.html")
    
