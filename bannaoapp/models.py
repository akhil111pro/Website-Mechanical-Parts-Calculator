from django.db import models
from django.contrib.auth.models import User #Create your models here.


class Orders(models.Model):
    orderedBy = models.CharField(max_length=50 ,editable=False)
    status = models.CharField(max_length=50)
    file = models.FileField(null=True , blank=True)
    volume = models.IntegerField(null=True , blank=True)
    weight = models.IntegerField(null=True , blank=True)
    calculatedPrice = models.IntegerField(null=True , blank=True)
    description = models.TextField(max_length = 100)
    
    class Meta:
        db_table = "orders"
    
    

    

    
    
