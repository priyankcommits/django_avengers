from django import forms

from web.models import Hero


class HeroForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    power = forms.IntegerField(label='Power', required=True)
    icon = forms.CharField(label='Icon', required=False)
    speciality = forms.CharField(label='Speciality', required=True)
    is_god = forms.BooleanField(label='Is god', required=False)


class HeroModelForm(forms.ModelForm):
    class Meta:
        model = Hero
        exclude = ['id']
