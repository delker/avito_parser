from django.shortcuts import render

from .forms import AvitoForm
from parsing.functions.parser import avito_pars
from django.http import HttpResponseRedirect
# Create your views here.


def main(request):
    results = []
    max_price = None
    if request.method == 'POST':
        form = AvitoForm(request.POST)
        if form.is_valid():
            base_url = form.cleaned_data['base_url']
            pages = form.cleaned_data['pages']
            kwords = form.cleaned_data['kwords']
            max_price = form.cleaned_data['max_price']
            results = avito_pars(base_url, pages, kwords)
    else:
        form = AvitoForm()
    context = {'form': form, 'results': results, 'max_price': max_price}
    return render(request, 'main.html', context)
