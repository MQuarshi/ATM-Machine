from django.db import models
from django.core.validators import RegexValidator
import random
import datetime
# Create your models here.
class ATM(models.Model):
    """Class that interacts with db to view and update a customer's balance"""
    def __init__(self, num):
        self.num = num

    def __unicode__(self):
        return self.num



class Account(models.Model):
    num = models.CharField(max_length=10,
                           validators=
                           [RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')]
                           )
    phonenum = models.CharField(max_length=7,
                                validators=
                                [RegexValidator(regex='^.{7}$', message='Length has to be 7', code='nomatch')]
                                )
    name = models.TextField()
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    owner = models.OneToOneField("User")
    ACCOUNT_TYPE = (
        ('SAVINGS', 'Savings'),
        ('CHECKING', 'Checking'),
    )

    account_type = models.CharField(
        max_length = 8, 
        choices=ACCOUNT_TYPE, 
        default='CHECKING',
    )

    def __unicode__(self):
        return ""


class ATMCard():
    name = models.CharField(max_length=50)
    account = models.ForeignKey(Account)
    dateofissue = models.DateField()
    expiration = models.DateField()
    num = models.IntegerField()
    pin = models.CharField(max_length=4,
                           validators=
                           [RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')]
                           )

    def __unicode__(self):
        return ("Name: {name}: Number: {num}".format(name=self.name, num=self.num) 
            + "Issue: "
            + self.dateofissue.strftime("%Y-%m-%d") 
            + " Expiration: " 
            + self.expiration.strftime("%Y-%m-%d")
            )

class User(models.Model):
    name = models.TextField()