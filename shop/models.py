from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxLengthValidator,MinLengthValidator 


STATE_CHOICES = (('Andaman &Nicobar Islands','Andaman &Nicobar Islands'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chandigarh','Chandigrah'),
('Chhattisgarh','Chhattisgarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Gujarat','Gujarat'),
('Rajasthan','Rajasthan'),
('Madhya Pradesh','Madhya Pradesh'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Jammu','Jammu'),
('haryana','Harayana'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Lakshadweep','Lakshadweep'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangan'),
('Tripura','Tripura'),
('Uttar Pradesh','Uttar Pradesh'),
('Delhi','Delhi'),
('west Bengal','Wesh Bangal'),
('Punjab','Punjab'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=200)
    
    def __str__(self) -> str:
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price=models.FloatField()
    description = models.TextField()
    brand= models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')
    
    def __str__(self) -> str:
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On The Way'),
    ('Delevered','Delevered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 
    
    