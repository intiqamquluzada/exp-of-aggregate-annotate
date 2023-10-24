from my_app.models import Product
from django.db.models import Max


def data_sender(request):
    max_price = Product.objects.aggregate(Max("count"))
    return {"max_price": max_price}
