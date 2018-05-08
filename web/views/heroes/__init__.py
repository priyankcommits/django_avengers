from django.shortcuts import render

from web.models import Hero


def list_heroes(request):
    template = 'hero/list.html'
    heroes = Hero.objects.all().order_by('-power')
    context = {
        'heroes': heroes,
    }
    return render(request, template, context)
