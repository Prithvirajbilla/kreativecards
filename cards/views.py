from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from cards.models import Card

def home(request):
	template = "home.html"
	# Do the query
	cards = Card.objects.filter(front_page=True,status=True)
	for card in cards:
		card.diff = card.prize-card.discount
	return render(request,template,{'cards':cards})
