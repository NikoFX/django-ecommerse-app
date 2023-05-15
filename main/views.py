from django.shortcuts import render
from django.http import HttpResponse
import random
from blogs.models import Blogs
from django.db.models import Q
from slider.models import Slider
from django.contrib import messages
from .models import Calls
from products.models import Popular
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def main(request):

    # popular products

    pp = Popular.objects.order_by('-id')[:10]

    # Slider
    s = Slider.objects.filter(Q(blog__company='all') | Q(blog__company='tepe'))
    # End Slider

    first = Blogs.objects.last()
    a = first.id-1
    b = first.id-2
    second = Blogs.objects.get(id=a)
    third = Blogs.objects.get(id=b)

    response = render(request, 'main/index.html', {'first':first, 'second':second, 'third':third, 's':s, 'pp':pp})

    # Zeng et xidmeti ucun POST
    if request.POST:
        fullname = request.POST.get('name', 0) + ' ' + request.POST.get('lastname', 0)
        phone = request.POST.get('phone', 0)
        message = request.POST.get('message', 0)
        s = (
            '+994',
            '994',
            '50',
            '050',
            '51',
            '051',
            '55',
            '055',
            '70',
            '070',
            '77',
            '077'
        )
        if phone.startswith(s):
            c = Calls(name=fullname, phone=phone, message=message)
            c.save()
        messages.success(request, 'Thank you!')

    # Saytı açan ilk usere random olaraq cookie_id verilir. Bir dəfə verilir. (Səbət üçün)
    rand_cookie = random.randint(7324, 999999999)
    if not request.COOKIES.get('guest_id'):
        response.set_cookie(key='guest_id', value=rand_cookie, max_age=1000000)
        return response
    else:
        return response
