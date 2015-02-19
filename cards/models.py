from django.db import models
from image_cropping import ImageRatioField

class Occassion(models.Model):
	title = models.CharField(max_length=255,null=True,blank=True)

	def __unicode__(self):
		return self.title


# Create your models here.
class Card(models.Model):
	title = models.CharField(max_length=255,null=True,blank=True)
	occassion = models.ForeignKey(Occassion,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	for_people = models.CharField(max_length=255,blank=True,choices=(('HER','HER'),
		('HIM','HIM'),('BOTH','BOTH')));
	prize = models.IntegerField(null=True,blank=True)
	discount = models.IntegerField(null=True,blank=True)
	status = models.BooleanField(blank=True)
	front_page = models.BooleanField(blank=True)
	number_of_pieces = models.IntegerField(null=True,blank=True)
	image1 = models.ImageField(blank=True, upload_to='uploaded_images')
	cropping = ImageRatioField('image1', '480x480',size_warning=True)
	image2 = models.ImageField(blank=True,upload_to='uploaded_images')
	image3 = models.ImageField(blank=True,upload_to='uploaded_images')

	def __unicode__(self):
		return self.title

class Customer(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	time = models.DateTimeField(auto_now_add=True)

class TotalOrder(models.Model):
	customer = models.ForeignKey(Customer)

class Order(models.Model):
	card = models.ForeignKey(Card)
	number = models.IntegerField(null=True,blank=True)
	total_order = models.ForeignKey(TotalOrder)

class TrackingStatus(models.Model):
	total_order = models.ForeignKey(TotalOrder)
	status = models.TextField()
