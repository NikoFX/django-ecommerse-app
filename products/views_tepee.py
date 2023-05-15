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

# Create your views here.
@register.filter
def get_range(value):
    return range(value)

def products(request):

    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe'))).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus, 'page_number': page_number})

def interdental(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & (Q(category='original') | Q(category='extra_soft') | Q(category='angle'))).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def original(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='original')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def extra_soft(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='extra_soft')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def angle(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='angle')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def toothpicks(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='toothpicks')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def dental_floss(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='dental_floss')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def brushers(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(Q(category='adult') | Q(category='kids'))).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def adult(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='adult')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def kids(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='kids')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def special_brushes(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='special_brushes')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def accesories(request):
    pr = Products.objects.filter(Q(status=True) & Q(Q(company='all') | Q(company='tepe')) & Q(category='accesories')).order_by('?')

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

    return render(request, 'products/tepe/templates/products/products.html', {'pr': pr, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus})

def add(request):

    product_id = request.GET.get('product_id', 1)
    count = int(request.GET.get('count', 1))
    cookie_id = request.COOKIES['guest_id']

    get_pr = Products.objects.get(id=product_id)
    def get_price():
        if get_pr.price_discount > 0:
            return get_pr.price_discount
        else:
            return get_pr.price
    # Eyni məhsulu əlavə edəndə, database də sadəcə məhsulun sayı ('count') update olunacaq!
    try:
        # update #
        gett = Basket.objects.get(cookie_id=cookie_id, product_id=product_id)
        c = gett.count
        tc = c + count
        if c > 0:
            gett.count = tc
            gett.save(force_update=True)
    except:
        # create #
        b = Basket(cookie_id=cookie_id, product_id=product_id, name=get_pr.name, size=get_pr.size, image=get_pr.image1, price=get_price(), count=count)
        b.save()

    messages.success(request, 'Added to basket!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def product_detail(request, product_id=0):

    pr = Products.objects.get(id=product_id)

    return render(request, 'products/tepe/templates/products/product_info.html', {'pr': pr})