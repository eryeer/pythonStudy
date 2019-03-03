from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo
from datetime import date, datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse


# Create your views here.
def index(request):
    # a = 'a'+1
    # print(BookInfo.objects.filter(heroinfo__hcomment__contains='八'))
    # print(HeroInfo.objects.filter(hbook__btitle='天龙八部'))
    book_infos = BookInfo.objects.all()
    return render(request, "booktest/index.html", {'books': book_infos})


def create(request):
    book_info = BookInfo()
    book_info.btitle = "射雕英雄传"
    book_info.bpub_date = date(1977, 1, 1)
    book_info.bcomment = 3
    book_info.save()
    return HttpResponseRedirect("/index")


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return redirect('/index')


def login(request):
    return render(request, "booktest/login.html")


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return redirect('/index')
    else:
        return render(request, "booktest/login.html", {'alert': 'user or password wrong'})


def ajax_login(request):
    return render(request, 'booktest/ajax_login.html')


def ajax_login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def set_cookie(request):
    res = HttpResponse('设置一个cookie')
    res.set_cookie('animal', 'cock', max_age=30 * 60)
    return res


def get_cookie(request):
    animal_ = request.COOKIES['animal']
    return HttpResponse(animal_)


def set_session(request):
    request.session['username'] = 'lalala'
    request.session['password'] = 'pwd'
    # request.session.set_expiry(50)
    return HttpResponse('set finish')


def get_session(request):
    username_ = request.session['username']
    password_ = request.session['password']
    return HttpResponse(username_ + ":" + password_)
