from django.shortcuts import render
from django.http import HttpResponse
from basket.models import Basket
from basket.models import Orders
from products.models import Products
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
import a

# Create your views here.

def basket(request):

    cookie_id = request.COOKIES['guest_id']


    bt = Basket.objects.filter(cookie_id=cookie_id)
    # Basketde mehsulun olub olmadigini yoxluyur
    r = 0
    for i in bt:
        r +=1
    ##########################################
    #Toplam qiymet
    price = 0
    for i in bt:
        price+=(i.price*i.count)

    ##########################################
    if r==0:
        return HttpResponseRedirect('../products')
    else:
        return render(request, 'basket/miradent/basket.html', {'bt': bt, 'cookie_id':cookie_id, 'price':price})

def refresh(request):

    cookie_id = request.COOKIES['guest_id']
    updating_id = request.POST.get('ref', None)
    count = request.POST.get('c', None)

    b = Basket.objects.get(cookie_id=cookie_id, product_id=updating_id)
    b.count = count
    b.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete(request):

    cookie_id = request.COOKIES['guest_id']
    deleting_id = request.GET.get('del', None)

    b = Basket.objects.get(cookie_id=cookie_id, product_id=deleting_id)
    b.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checkout(request):

    #### Sifariş təstiqləmə POST

    cookie_id = request.COOKIES['guest_id']

    name = request.POST.get('name', 0)
    lastname = request.POST.get('lastname', 0)
    phone = request.POST.get('phone', 0)
    address = request.POST.get('address', 0)

    if request.POST:

        products = Basket.objects.filter(cookie_id=cookie_id)
        text = ''
        e_text = ''
        for i in products:
            text += '{}  ({} ədəd)\n'.format(i.name, i.count)
            e_text += '{}  ({} ədəd)<br>'.format(i.name, i.count)

        #string = '{} {} Tel: {} Ünvan: {}'.format(name, lastname, phone, address)
        fullname = name+' '+lastname
        order = Orders(name=fullname, phone=phone, address=address, product=text)
        order.save()

        mess = '<h2>Adı:  {}<br>Soyadı:  {}<br>Tel:  {}<br>Ünvanı:  {}<br>Sifarişlər: <br>{}</h2>'.format(name, lastname, phone, address, e_text)
        a.send(mess)

        messages.success(request, 'Your order has been recorded.Thank you')
        return redirect('/miradent/products/')

    return render(request, 'basket/miradent/checkout.html', )