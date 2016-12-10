from django.shortcuts import render
from django_web.models import Misc
from django import template
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    limit = 4
    MiscInfo = Misc.objects[:4]
    paginatior = Paginator(MiscInfo,limit)
    page = request.GET.get('page')
    try:
        loaded = paginatior.page(page)
        Range = reversed(list(range(loaded.number,loaded.number + 5)))
        context = {
            'Misc':loaded,
            'Rang':Range
        }
        print(page)
    except PageNotAnInteger:
        loaded = paginatior.page(1)
        Range = reversed(list(range(loaded.number, loaded.number + 5)))
        context = {
            'Misc': loaded,
            'Rang': Range
        }
    except EmptyPage:#判断是否空值，否则返回最后一页
        loaded = paginatior.page(1)
        Range = reversed(list(range(loaded.number, loaded.number + 5)))
        context = {
            'Misc': loaded,
            'Rang': Range
        }
    return render(request,'blog.html',context)
def blogViws(request):
    return render(request,'blogsingle.html')