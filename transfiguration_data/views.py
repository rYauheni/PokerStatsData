from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from .models import Title, Data
from .forms import InputDataForm
from .utils import SEPARATOR, transfigurate


# Create your views here.

class IndexView(FormView):
    template_name = 'transfiguration_data/index.html'
    form_class = InputDataForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        form.full_clean()
        self.request.session.set_expiry(3600)
        self.request.session['input_data'] = form.cleaned_data
        self.request.session['existence'] = True
        url = reverse('transfiguration_url')
        return redirect(url)


class TransfigurationView(View):
    def get(self, request):
        if 'existence' in request.session:
            input_data = request.session.get('input_data')
            input_data = input_data['input_data']
            titles = Title.objects.exclude(priority__isnull=True).order_by('priority')
            output_data = transfigurate(input_data=input_data, titles=titles)
            return render(request, 'transfiguration_data/transfiguration.html', context={
                'output_data': output_data,
                'separator': SEPARATOR,
            })
        else:
            raise Http404
