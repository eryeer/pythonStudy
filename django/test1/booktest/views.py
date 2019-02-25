from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, HeroInfo


# Create your views here.

def index(request):
    """
    # 1.获取模板
    template = loader.get_template('booktest/index.html')
    # 2.定义上下文
    context = RequestContext(request, {'title': '图书列表', 'list': range(10)})
    # 3.渲染模板
    return HttpResponse(template.render(context))
    """
    booklist = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'booklist': booklist})


def show_heros(request, bid):
    book = BookInfo.objects.get(id=bid)
    herolist = book.heroinfo_set.all()
    return render(request, 'booktest/show_hero.html',
                  {'btitle': book.btitle, 'herolist': herolist})
