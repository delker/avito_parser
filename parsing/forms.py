from django import forms


class AvitoForm(forms.Form):
    base_url = forms.CharField(widget=forms.TextInput(attrs=({'size': '100%'})))
    pages = forms.IntegerField(label='Количество страниц', initial=1)
    kwords = forms.CharField(label='Ключевое слово')
    max_price = forms.IntegerField(label='Максимальная цена')
