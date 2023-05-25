from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Land

class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'

class LandDetailView(DetailView):
    model = Land
    template_name = 'land/land_detail.html'

class LandeCreateView(CreateView):
    model = Land
    template_name = 'land/land_create.html'
    fields= '__all__'