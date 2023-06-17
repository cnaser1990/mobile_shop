from django.shortcuts import render
from .models import Mobile
from django.views.generic import ListView , DetailView


# Create your views here.

class MobileList(ListView):
    model=Mobile
    template_name='mobiles.html'
    context_object_name='mob'


class MobileDetail(DetailView):
    model = Mobile
    template_name='detail.html'
    context_object_name='detail'
