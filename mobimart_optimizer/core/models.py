from django.db import models

class Store(models.Model):
    STORE_TYPES = (
        ('TIER_1', 'Bangalore Flagship / High Footfall'),
        ('TIER_2_3', 'Tier-2/3 Regional (Mysore, Hubli, etc.)'),
    )
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    tier = models.CharField(max_length=10, choices=STORE_TYPES)
    monthly_budget_weight = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.name} ({self.city})"

class PhoneModel(models.Model):
    CATEGORY_CHOICES = (
        ('BUDGET', 'Budget Phone (₹6k - ₹15k)'),
        ('MID', 'Mid-Range (₹15k - ₹40k)'),
        ('FLAGSHIP', 'Flagship (₹40k - ₹1.5L)'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    launch_week = models.IntegerField(default=1)  # Week 1 to 52
    successor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_eol = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SalesRecord(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    week_number = models.IntegerField()
    units_sold = models.IntegerField(default=0)
    stock_available = models.IntegerField(default=0)

class InventoryAllocation(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    phone = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    week_number = models.IntegerField()
    allocated_units = models.IntegerField()
    capital_allocated = models.DecimalField(max_digits=12, decimal_places=2)
    reasoning_rupees = models.TextField()