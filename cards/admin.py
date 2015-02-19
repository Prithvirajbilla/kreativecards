from django.contrib import admin
from image_cropping import ImageCroppingMixin,ImageCropWidget
from cards.models import *

from django import forms
from image_cropping import ImageCropWidget

class MyModelForm(forms.ModelForm):
	class Meta:
		widgets = {'image1': ImageCropWidget}


class CardAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = MyModelForm

admin.site.register(Card,CardAdmin)
admin.site.register(Occassion)