from django.shortcuts import render,redirect
from booktest.models import BookInfo, HeroInfo
from datetime import date
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    book_infos = BookInfo.objects.all()
    return render(request, "booktest/index.html", {'books': book_infos})


def create(request):
    book_info = BookInfo()
    book_info.btitle = "射雕英雄传"
    book_info.bpub_date = date(1977, 1, 1)
    book_info.bcomment = 3
    book_info.save()
    return HttpResponseRedirect("/index")

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return redirect('/index')