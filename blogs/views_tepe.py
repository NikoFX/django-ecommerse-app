from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.defaulttags import register
from .models import Blogs

# Create your views here.

@register.filter
def get_range(value):
    return range(value)

def blogs(request):

    if request.GET.get('blog', False):
        b = Blogs.objects.get(id=request.GET.get('blog', False))
        return render(request, 'blogs/tepe/blog.html', {'b': b})

    else:

        bg = Blogs.objects.filter(Q(company='all') | Q(company='tepe'))

        paginator = Paginator(bg, 1)  # Show 1 contacts per page.
        page_number = request.GET.get('page', 1)
        bg = paginator.get_page(page_number)
        pg = paginator.num_pages + 1

        if int(page_number) > 1:
            pageminus = int(page_number) - 1
        else:
            pageminus = int(page_number)

        if int(page_number) <= (pg - 5):
            pageplus = int(page_number) + 1
        else:
            pageplus = pg - 1

        return render(request, 'blogs/tepe/blogs.html', {'bg':bg, 'pg': pg, 'pageminus': pageminus, 'pageplus': pageplus, 'page_number': page_number})