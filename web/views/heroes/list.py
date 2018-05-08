from django.shortcuts import render
from django.views.generic import View

from web.models import Hero


class HeroListView(View):

    def get(self, request, template='hero/list.html', *args, **kwargs):
        heroes = Hero.objects.all().order_by('-power')
        context = {
            'heroes': heroes,
        }
        return render(request, template, context)
