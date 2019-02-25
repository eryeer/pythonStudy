from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender','hage','hcomment','hbook']


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
