from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class StockInfo(models.Model):
    stock_id = models.IntegerField(default=0)
    company_name = models.CharField(max_length=50)
    growth_rate = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s' % (self.stock_id, self.company_name, self.growth_rate)