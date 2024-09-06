from django.contrib import admin
from .models import ProductCategory,Product,ProductImage,ProductOffer, OfferProductNews,TrendingProduct
# Register your models here.
from .models import MostSoldProduct,ProductLog

from .models import FeaturedProduct
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductOffer)
admin.site.register(OfferProductNews)
admin.site.register(FeaturedProduct)
admin.site.register(TrendingProduct)
admin.site.register(MostSoldProduct)
admin.site.register(ProductLog)