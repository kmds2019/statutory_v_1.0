from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import statutory_details,countries,domain
from .forms import StatutoryDetailsInputForm


class StatutoryDetailsListView(ListView):
    model = statutory_details
    context_object_name = 'statutory_details_list'


class StatutoryDetailsCreateView(CreateView):
    model = statutory_details
    form_class = StatutoryDetailsInputForm
    success_url = reverse_lazy('display_statutory_list')


class StatutoryDetailsUpdateView(UpdateView):
    model = statutory_details
    form_class = StatutoryDetailsInputForm
    success_url = reverse_lazy('display_statutory_list')

def LoadCountries(request):
    countries = countries.objects.all()
    return render(request, 'countries_dropdown_list_options.html', {'countries': countries})

def LoadDomains(request):
    country_id = request.GET.get('country')
    domains = domain.objects.filter(country_id=country_id).order_by('domain_name')
    return render(request, 'domains_dropdown_list_options.html', {'domains': domains})

"""
def LoadActs(request):
    domain_id = request.GET.get('domain')
    acts = tbl_act.objects.filter(domain_id=domain_id).order_by('act_name')
    return render(request, 'acts_dropdown_list_options.html', {'acts': acts})
"""

#below function is only temporary, once acts model is ready, it has to be replaced with the above function
def LoadActs(request):
    country_id = request.GET.get('country')
    domains = domain.objects.filter(country_id=country_id).order_by('domain_name')
    return render(request, 'acts_dropdown_list_options.html', {'domains': domains})
