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
        return self.company_name

class FinancialProduct(models.Model):
    fp_id = models.IntegerField(default=0)

class StructuredFinancialInvestment(models.Model):
    fp_id = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, verbose_name="the financial product id")
    stock_id = models.ForeignKey(StockInfo, on_delete=models.CASCADE, verbose_name="the stock id")
    SFI_id = models.IntegerField(default=0)
    Knock_in = models.IntegerField(default=0)
    Knock_out = models.IntegerField(default=0)
    put_strike = models.IntegerField(default=0)





