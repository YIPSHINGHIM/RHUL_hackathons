from django.db import models

# Create your models here.


class Account_Holder(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='account_holder')
    social_media = models.URLField()
    profit = models.CharField(max_length=100)
    bank_acc = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    followers = models.PositiveBigIntegerField()
    about = models.TextField()

    def __repr__(self):
        return self.name