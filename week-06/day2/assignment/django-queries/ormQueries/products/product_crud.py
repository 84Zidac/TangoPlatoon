from .models import Product 
from django.db.models import Q, Avg, Max
from statistics import mean
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod 
    def find_by_model(cls, name):
        return Product.objects.filter(model=name).first()
    
    @classmethod
    def last_record(cls):
        return Product.objects.last()
    
    @classmethod
    def by_rating(cls, query_rating):
        return Product.objects.filter(rating=query_rating)
    
    @classmethod
    def by_rating_range(cls, lower, upper):
        return Product.objects.filter(rating__gte=lower, rating__lte=upper)
    
    @classmethod
    def by_rating_and_color(cls, query_rating, query_color):
        return Product.objects.filter(rating=query_rating, color=query_color)
    
    @classmethod
    def by_rating_or_color(cls, query_rating, query_color):
        return Product.objects.filter(Q(rating=query_rating) | Q(color=query_color))

        
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()
    
    @classmethod
    def below_price_or_above_rating(cls, below_price, above_rating):
        return Product.objects.filter(Q(price_cents__lte=below_price) | Q(rating__gte=above_rating))
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by('category', '-price_cents')
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls, srch_name):
        return Product.objects.filter(manufacturer__contains=srch_name)
    
    @classmethod
    def manufacturer_names_for_query(cls, srch_name):
        list = Product.objects.filter(manufacturer__contains=srch_name)
        return_list = []
        for itm in list:
            return_list.append(itm.manufacturer)
        return return_list

        # return [itm.manufacturer for itm in Product.objects.filter(manufacturer__contains=srch_name)]
    @classmethod
    def not_in_a_category(cls, cat_name):
        return Product.objects.exclude(category=cat_name)
    
    @classmethod
    def limited_not_in_a_category(cls, cat_name, limit):
        return Product.objects.exclude(category=cat_name)[:limit]
    
    @classmethod
    def category_manufacturers(cls, cat_name):
        return [itm.manufacturer for itm in Product.objects.filter(category=cat_name)]
        
    @classmethod
    def average_category_rating(cls, cat_name):
        return Product.objects.filter(category=cat_name).aggregate(Avg('rating'))
        # print(mean([itm.rating for itm in Product.objects.filter(category=cat_name)]))
        # return mean([itm.rating for itm in Product.objects.filter(category=cat_name)])

    @classmethod
    def greatest_price(cls):
        return Product.objects.all().aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        lst = [(x.model, x.pk) for x in Product.objects.all()]
        return max(lst, key=lambda x: len(x[0]))[1]

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.all().order_by(Length('model'))