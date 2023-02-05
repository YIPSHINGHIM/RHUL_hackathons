from django.db import models

# Create your models here.

#asdf


class Account_Holder(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='account_holder')
    social_media = models.URLField()
    profit = models.CharField(max_length=100)
    bank_acc = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    followers = models.PositiveBigIntegerField()
    about = models.TextField()

    # ts_id = models.CharField(max_length=50)
    # ts_date = models.DateTimeField('transaction date')
    # ts_amount = models.IntegerField(default = 0)

    def __repr__(self):
        return self.name

class CompanyInfo(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length=100)
    about = models.TextField()
    total_ads = models.IntegerField(default = 0)

    def __repr__(self):
        return self.name