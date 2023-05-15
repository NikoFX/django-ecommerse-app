from django.shortcuts import render
from django.http import HttpResponse
from basket.models import Basket
from basket.models import Orders
from basket.models import Coupons, Coupon_holders, Min_order
from products.models import Products
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from decimal import Decimal
import math
import a


# Create your views here.

def basket(request):
    cookie_id = request.COOKIES['guest_id']

    coupon_name = ''
    coupon_including = 500
    coupon_discount = 0
    discount = False


    # Minimum Order
    try:
        m_o = Min_order.objects.get(id=1)
        delivery_price = m_o.delivery_price
        min_order = m_o.price
    except:
        s = Min_order(id=1)
        s.save()
    ###
     ####/******
    try:
        ch = Coupon_holders.objects.get(cookie_id=cookie_id)
    except:
        ch = Coupon_holders(cookie_id=cookie_id, coupon=None)
        ch.save()
     #####/******
    # Show Discount
    ccc = Coupons.objects.all()
    try:
        ch = Coupon_holders.objects.get(cookie_id=cookie_id)
        cc = Coupons.objects.all()
    except:
        ch = None
        cc = None

    if ch != None and cc != None:
        ll = list(cc)
        if not ccc:
            # Clear Coupon Holders (Because, It's not a Foreignkey and not depending on Coupons)
            print(55555555555)
        else:
            print(55555555555)
        for i in ll:
            if i.coupon_code == ch.coupon:
                coupon_name = i.coupon_code
                coupon_discount = i.discount
                coupon_including = i.including
                print(4645)
            else:
                # Clear Coupon Holders (Because, It's not a Foreignkey and not depending on Coupons)
                print(666)


    else:
        discount = False
    ######


    # Show discount on price


    bt = Basket.objects.filter(cookie_id=cookie_id)

    # Basketde mehsulun olub olmadigini yoxluyur
    r = 0
    for i in bt:
        r += 1
    ##########################################
    # Toplam qiymet
    price = 0
    old_price = 0
    for i in bt:
        price += (i.price * i.count)
    old_price = price

    if coupon_including <= price:
        price = price - (price * coupon_discount / 100)

    old_price = math.ceil(old_price*100)/100
    price = math.ceil(price*100)/100

    if price < min_order:
        price += delivery_price

    ##########################################
    if r == 0:
        return HttpResponseRedirect('../products')
    else:
        return render(request, 'basket/basket.html', {'bt': bt, 'cookie_id': cookie_id, 'old_price': old_price, 'discount': discount, 'price': price, 'coupon_name': coupon_name, 'coupon_including': coupon_including,  'coupon_msg': coupon_discount, 'min_order': min_order, 'delivery_price': delivery_price})


def refresh(request):
    cookie_id = request.COOKIES['guest_id']
    updating_id = request.POST.get('ref', None)
    count = request.POST.get('c', None)

    b = Basket.objects.get(cookie_id=cookie_id, id=updating_id)
    b.count = count
    b.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete(request):
    cookie_id = request.COOKIES['guest_id']
    deleting_id = request.GET.get('del', None)

    b = Basket.objects.get(cookie_id=cookie_id, id=deleting_id)
    b.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkout(request):


    #### Sifariş təstiqləmə POST


    cookie_id = request.COOKIES['guest_id']

    name = request.POST.get('name', 0)
    lastname = request.POST.get('lastname', 0)
    phone = request.POST.get('phone', 0)
    address = request.POST.get('address', 0)

    ### Coupon discount
    try:
        ch = Coupon_holders.objects.get(cookie_id=cookie_id)
        cc = Coupons.objects.all()
    except:
        ch = None
        cc = None
    coupon_including = 0
    coupon_discount = 0
    if ch != None and cc != None:
        ll = list(cc)
        for i in ll:
            if i.coupon_code == ch.coupon:
                coupon_including = i.including
                coupon_discount = i.discount
    ###########

        # Minimum Order
    dd = 0
    try:
        m_o = Min_order.objects.get(id=1)
        delivery_price = m_o.delivery_price
        min_order = m_o.price
    except:
        s = Min_order(id=1)
        s.save()
        ###

    if request.POST:

        products = Basket.objects.filter(cookie_id=cookie_id)
        text = ''
        e_text = ''
        p_color = 'Standart'
        old_toplam_msg = ''
        toplam = 0.0
        tt = 0.0
        pp = 0.0
        for i in products:
            if i.color_purple is True:
                p_color = 'Fiolet'
            if i.color_green is True:
                p_color = 'Green'
            if i.color_yellow is True:
                p_color = 'Yellow'
            if i.color_blue is True:
                p_color = 'Blue'
            if i.color_black is True:
                p_color = 'Black'
            if i.color_grey is True:
                p_color = 'Silver'
            if i.color_red is True:
                p_color = 'Red'
            if i.color_pink is True:
                p_color = 'Pink'
            if i.color_orange is True:
                p_color = 'Orange'
            if i.color_mix is True:
                p_color = 'Mix'
            pp = i.price
            tt = pp * Decimal(i.count)
            toplam = Decimal(toplam) + tt
            toplam = math.ceil(toplam * 100) / 100

            if coupon_including <= toplam:
                old_toplam_msg = 'Total: {} azn'.format(toplam)
                toplam = toplam - (toplam * coupon_discount / 100)
            toplam = math.ceil(toplam * 100) / 100
            pp = math.ceil(pp * 100) / 100

            text += '{},  ({}, {} count)  -  {} azn\n'.format(i.name, p_color, i.count, pp)
            e_text += '<hr>{},  ({}, {} count)  -  <span style="color:green;">{} azn</span><br>'.format(i.name, p_color,
                                                                                                       i.count, pp)
        # string = '{} {} Tel: {} Ünvan: {}'.format(name, lastname, phone, address)

        coupon_txt = ''
        if ch != None and coupon_including <= toplam:
            coupon_txt = '(Coupon code: {}, discount: {}%) \n'.format(ch.coupon, coupon_discount)

        if toplam < min_order:
            toplam += delivery_price
        else:
            delivery_price = 0

        fullname = name + ' ' + lastname
        text += '{}\n\n{}Delivery fee: {} azn\n\n Total: {} azn'.format(old_toplam_msg, coupon_txt, delivery_price, toplam)
        order = Orders(name=fullname, phone=phone, address=address, product=text)
        order.save()

        mess = '<h2><i>First Name:</i>  {}<br><i>Last Nameyadı:</i>  {}<br><i>Tel no:</i>  {}<br><i>Address:</i>  {}<br><i>Orders:</i> <br>{} <hr>{} <br> {}<br> Delivery fee {} azn <hr> <i>Total:</i> <span style="color:green;">{} azn</span></h2>'.format(
            name, lastname, phone, address, e_text, old_toplam_msg, coupon_txt, delivery_price, toplam)
        a.send(mess)

        messages.success(request, 'Your order has been recorded. Thank you')
        return redirect('/products/')

    return render(request, 'basket/checkout.html', )


def coupon_check(request):

    cookie_id = request.COOKIES['guest_id']
    code = request.POST.get('code', 0)
    s = False



    ch = Coupon_holders.objects.get(cookie_id=cookie_id)

    c = Coupons.objects.all()
    c = list(c)

    ch.coupon = code
    ch.save()

    for i in c:
        if code == i.coupon_code:
            s = True
            ch.coupon = code
            ch.save()
        else:
            s = False


    if request.POST:

        if s is True:
            messages.success(request, 'The coupon has been added!')
        else:
            messages.error(request, 'Wrong coupon code')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
