from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View

from web.forms import HeroForm, HeroModelForm
from web.models import Hero


class HeroCreateView(View):

    def get(self, request, template='hero/create.html', *args, **kwargs):
        form = HeroForm()
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, template='hero/create.html', *args, **kwargs):
        form = HeroForm(data=request.POST)
        if form.is_valid():
            Hero.objects.create(
                name=form.cleaned_data['name'],
                power=form.cleaned_data['power'],
                icon=form.cleaned_data['icon'],
                is_god=form.cleaned_data['is_god'],
            )
            return HttpResponseRedirect(reverse("web:hero_list"))
        context = {
            'form': form,
        }
        return render(request, template, context)


class HeroCreateModelView(View):

    def get(self, request, template='hero/create.html', *args, **kwargs):
        form = HeroModelForm()
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, template='hero/create.html', *args, **kwargs):
        form = HeroModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("web:hero_list"))
        context = {
            'form': form,
        }
        return render(request, template, context)
