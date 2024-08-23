from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from .models import ProductCategory,Product,ProductImage,ProductOffer,TrendingProduct
from django.contrib import messages

from django.http import JsonResponse
from django.core import serializers
from .forms import ProductCategoryForm,ProductForm,ProductImageForm
from .serializers import ProductOfferSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from .paginations import StandardResultsSetPagination
from .models import OfferProductNews,FeaturedProduct,MostSoldProduct



def product_category(request):
    context={}
    if request.method=="POST":
    
        action = request.POST.get('action',None)
        if action=="remove":
            category_id= request.POST.get('category_id',None)
            if category_id is not None and category_id != "":
                obj=ProductCategory.objects.filter(id=category_id)
                if obj.exists():
                    name=obj[0].name
                    obj[0].delete()
                    messages.success(request, "Removed {} from Product Category".format(name))
                else:
                    messages.warning(request, "Please try to remove exitsing product category")
            else:
                messages.warning(request, "Please try to remove exitsing  category")
        
        elif action=="update":
            category_id= request.POST.get('category_id',None)
            if category_id is not None and category_id != "":
                update_form = ProductCategoryForm(request.POST)
                if update_form.is_valid():
                    obj=ProductCategory.objects.filter(id=category_id)
                    if obj.exists():
                        temp=obj[0]
                        old_name=temp.name
                        temp.name=update_form.cleaned_data["name"]
                        temp.save()
                        messages.success(request,"Succssfully category updated from {} to {} ".format(old_name,temp.name))
                    else:
                        messages.warning(request, "Unable to update due to the non-existance of this category")
                else:
                    messages.warning(request,"same category is already exits")
               
        elif action=="create":
            category= request.POST.get('name',None)
            if category is not None and category != "":
                create_form = ProductCategoryForm(request.POST)
                if create_form.is_valid():
                    create_form.save()
                    messages.success(request, "Added '{}' to Product Category".format(category))
                else:
                    context['create_form']=create_form      
        categories=ProductCategory.objects.all()
        
    elif request.method=="GET":
        action= request.GET.get('action',None)
        if action=="search":
            category=request.GET.get("category",None)
            if category is not None and category is not "":
                context['search_category']=category
                categories=ProductCategory.objects.filter(name__contains=category)
            else:
                categories=ProductCategory.objects.all()
        else:
            categories=ProductCategory.objects.all()

    context['categories']=categories
    return render(request,"product/category.html",context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            # print("error1")
            product=form.save()
            messages.success(request,"successfully created")
            return redirect(f'/dashboard/product/{product.id}/images/add')
    else:
        form = ProductForm()
    return render(request, 'product/create/specification.html', {'form': form})


def add_product_images(request,product_id):

    context={}
    product = Product.objects.get(id=product_id)
    context['product']=product
    if request.method == 'POST':
        action=request.POST.get("action" ,None)
        image_id=request.POST.get("image_id",None)
        if action=="remove" and image_id != "" and image_id is not None:
            images=ProductImage.objects.filter(product=product,id=image_id)
            if images.exists():
                image=images[0]
                image.delete()
                messages.success(request,"successfully removed")
                return redirect(f'/dashboard/product/{product.id}/images/add')

        else:
            image_form = ProductImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.product = product
                image.save()
                return redirect(f'/dashboard/product/{product.id}/images/add')
            context['image_form']=image_form
    else:
        context['image_form'] = ProductImageForm()
    context['images'] = product.images.all()
    return render(request, 'product/create/images.html', context)


def home(request):
    products=Product.objects.all()
    offer_products_news=OfferProductNews.objects.filter(active=True)
    offered_products=ProductOffer.objects.filter(status=True)
    featured_products=FeaturedProduct.objects.filter(active=True)
    trending_products=TrendingProduct.objects.filter(active=True)
    most_sold_products=MostSoldProduct.objects.filter(active=True)
    print(offer_products_news)
    context={"products":products,'offer_products_news':offer_products_news,
        'featured_products':featured_products,"offered_products":offered_products}
    context['trending_products']=trending_products
    context['most_sold_products']=most_sold_products
    return render(request,"product/view/home.html",context)

def detail(request,product_id):
    context={}
    product = Product.objects.get(id=product_id)
    context['product']=product
    return render(request,"product/view/detail.html",context)




@api_view(['GET','POST'])
def product_offer(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_query = request.GET.get("query", "")
        if search_query:
            offers = ProductOffer.objects.filter(product__name__icontains=search_query)
        else:
            offers = ProductOffer.objects.all()

        serializer = ProductOfferSerializer(offers, many=True)
        print(serializer.data)
        return Response(serializer.data)

    context = {}
    offers = ProductOffer.objects.all()
    context['offers'] = offers
    return render(request, "product/offer.html", context)


@api_view(['GET', 'POST'])
def product_offer(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_query = request.GET.get("query", "")
        paginator = StandardResultsSetPagination()
        
        if search_query:
            offers = ProductOffer.objects.filter(product__name__icontains=search_query)
        else:
            offers = ProductOffer.objects.all()

        result_page = paginator.paginate_queryset(offers.order_by('-updated_at'), request)
        serializer = ProductOfferSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    context = {}
    offers = ProductOffer.objects.all()
    context['offers'] = offers
    return render(request, "product/offer.html", context)