from django.db import models
from discos.models import Disco
from django import forms


class FormDisco(forms.ModelForm):
    class Meta:
        model = Disco
        exclude = ()
