from django.db import models


# 一类
# Create your models here.
class BookInfo(models.Model):
    # 字符串并指定最大长度
    btitle = models.CharField(max_length=20)
    # 日期
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


# 多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hage = models.IntegerField()
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname
