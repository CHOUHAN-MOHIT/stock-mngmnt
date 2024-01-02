from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    portfolio_value = models.DecimalField(max_digits=8, decimal_places=2)
    date_purchased = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.symbol} ({self.name})"

    def update_portfolio_value(self):
        self.portfolio_value = self.quantity * self.current_price
        self.save()
