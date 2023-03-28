from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Title, Data
from .forms import InputDataForm
from .utils import SEPARATOR, transfigurate


# Create your views here.

def index(request):
    form = InputDataForm()
    if request.method == 'GET':
        return render(request, 'TransfigurationData/index.html', context={
            'form': form,
        })
    elif request.method == 'POST':
        form = InputDataForm(request.POST)
        url = reverse('index_url')
        if form.is_valid():
            form.save()
            form.full_clean()
            request.session.set_expiry(3600)
            request.session['input_data'] = form.cleaned_data
            request.session['existence'] = True
            url = reverse('transfiguration_url')

        return redirect(url)


def transfiguration_data(request):
    if 'existence' in request.session:
        input_data = request.session.get('input_data')
        input_data = input_data['input_data']
        titles = Title.objects.exclude(priority__isnull=True).order_by('priority')
        output_data = transfigurate(input_data=input_data, titles=titles)
        return render(request, 'TransfigurationData/transfiguration.html', context={
            'output_data': output_data,
            'separator': SEPARATOR,
        })
    else:
        raise Http404
