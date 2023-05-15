from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from products.models import Products
from basket.models import Basket
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.defaulttags import register
from django.contrib import messages
import random
import time


# Create your views here.
@register.filter
def get_range(value):
    return range(value)


def products(request):



    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')))

    if request.GET.get('search', 0):
        pr = Products.objects.filter(Q(status=True) & Q(name__icontains=request.GET['search']) & Q(Q(company='all') | Q(company='tepe')))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages+1

    if int(page_number)>1:
        pageminus = int(page_number)-1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg-5):
        pageplus = int(page_number)+1
    else:
        pageplus = pg-1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus, 'page_number': page_number})

def interdental(request):
    pr = Products.objects.filter(status=True, category='interdental')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def original(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='original'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def extra_soft(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='extra_soft'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def angle(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='angle'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def toothpicks(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='toothpicks'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def dental_floss(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='dental_floss'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def brushers(request):
    pr = Products.objects.filter(status=True, category='brushers')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def adult(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='adult'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def kids(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='kids'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def special_brushes(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='special_brushes'))

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def accesories(request):
    pr = Products.objects.filter(status=True, category='accesories')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})
def tepe(request):
    pr = Products.objects.filter(status=True, company='tepe')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def miradent(request):
    pr = Products.objects.filter(status=True, company='miradent')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def aquapick(request):
    pr = Products.objects.filter(status=True, company='aquapick')

    paginator = Paginator(pr, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page', 1)
    pr = paginator.get_page(page_number)
    pg = paginator.num_pages + 1
    if int(page_number) > 1:
        pageminus = int(page_number) - 1
    else:
        pageminus = int(page_number)

    if int(page_number) <= (pg - 5):
        pageplus = int(page_number) + 1
    else:
        pageplus = pg - 1

    return render(request, 'products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def add(request):

    product_id = request.GET.get('product_id', 1)
    count = int(request.GET.get('count', 1))
    color = request.GET.get('color', 1)
    cookie_id = request.COOKIES['guest_id']

    fiolet=0
    green=0
    yellow=0
    blue=0
    black=0
    silver=0
    red=0
    pink=0
    orange=0
    mix=0

    if color=='fiolet':
        fiolet = 1
    if color=='green':
        green = 1
    if color=='yellow':
        yellow = 1
    if color=='blue':
        blue = 1
    if color=='black':
        black = 1
    if color=='silver':
        silver = 1
    if color=='red':
        red = 1
    if color=='pink':
        pink = 1
    if color=='orange':
        orange = 1
    if color=='mix':
        mix = 1

    get_pr = Products.objects.get(id=product_id)

    if color == 1 and get_pr.color == 'Qarisiq':
        messages.error(request, '<div class="alert alert-warning" role="alert">Choose the color!</div>')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get_price():
        if get_pr.price_discount > 0:
            return get_pr.price_discount
        else:
            return get_pr.price
    # Eyni məhsulu əlavə edəndə, database də sadəcə məhsulun sayı ('count') update olunacaq!
    try:
        # update #
        gett = Basket.objects.get(
            cookie_id=cookie_id,
            product_id=product_id,
            color_purple=fiolet,
            color_green=green,
            color_yellow=yellow,
            color_blue=blue,
            color_black=black,
            color_grey=silver,
            color_red=red,
            color_pink=pink,
            color_orange=orange,
            color_mix=mix
        )
        c = gett.count
        tc = c + count
        if c > 0:
            gett.count = tc
            gett.save(force_update=True)
    except:
        # create #
        b = Basket(cookie_id=cookie_id,
                   product_id=product_id,
                   name=get_pr.name,
                   size=get_pr.size,
                   image=get_pr.image1,
                   price=get_price(),
                   count=count,
                   color_purple=fiolet,
                   color_green=green,
                   color_yellow=yellow,
                   color_blue=blue,
                   color_black=black,
                   color_grey=silver,
                   color_red=red,
                   color_pink=pink,
                   color_orange=orange,
                   color_mix=mix
                   )
        b.save()

    messages.success(request, '<div class="alert alert-success" role="alert">Added to the baske!</div>')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def product_detail(request, product_id=0):

    pr = Products.objects.get(id=product_id)

    return render(request, 'products/product_info.html', {'pr': pr})