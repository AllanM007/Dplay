from django.shortcuts import render
from .models import Track
from django.views.generic import TemplateView

class HomeView(TemplateView):

	template_name = 'boomx/home.html'

	def get_context_data(self, *args, **kwargs):

		context = super(HomeView, self).get_context_data()

		context['tracks'] = Track.objects.all().order_by('-created_on')

		return context