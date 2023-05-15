from products.models import Products

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        dis_products = Products.objects.filter(price_discount__gt=0.00)
        dis_productss = Products.objects.filter(price_discount=0.00)
        for i in dis_products:
            i.discount = 1
            i.save()
        for i in dis_productss:
            i.discount = 0
            i.discount_precent=0
            i.save()
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware