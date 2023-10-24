from django.shortcuts import render
from my_app.models import Product
from django.db.models import Avg, Min, Max, Count



def index_view(request):
    # AGGREGATE
    # ANNOTATE
    min_price = Product.objects.aggregate(min_value=Min("price"))
    print(min_price)

    avg_price = Product.objects.aggregate(avg_price=Avg("price"))
    print(avg_price)


    count_of_objects = Product.objects.all().count()
    print(count_of_objects)

    my_objs = Product.objects.annotate(count_m=Count("material"))
    print(my_objs)

    my_products = Product.objects.filter(price__lte=50)
    print(my_products)

    # my_objss = Product.objects.order_by("name")

    context = {
        "min_price": min_price,
        "my_objs": my_objs,
    }
    return render(request, "index.html", context)
