# Copyright (c) 2019-2020 Eugene Davies All Rights Reserved. Some HTML pages are purely created for test purpose and are not the best views I would suggest

from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']