from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Products(models.Model):
    CAT=((1,'Collars,Leashes&Harnesses'),(2,'Food'),(3,'Cloth'),(4,'Toys'),(5,'Health&Hygienes'),
         (6,'Bowls&Feeders'),(7,'Pharmacy'))
    name=models.CharField(max_length=500,verbose_name='Product Name')
    price=models.FloatField()
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    pdetail=models.CharField(max_length=50000,verbose_name="Product Detail")
    pimage=models.ImageField(upload_to='images')
    is_active=models.BooleanField(default=True)


    '''   
    def __str__(self):
        #return self.name
        return self.price
        '''
  
   

class Cart(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('Products',on_delete=models.CASCADE,db_column='pid') 
    qty=models.IntegerField(default=1)


class Order(models.Model):
    orderid=models.CharField(max_length=50)
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('Products',on_delete=models.CASCADE,db_column='pid') 
    qty=models.IntegerField(default=1)
    amt=models.FloatField()  


         