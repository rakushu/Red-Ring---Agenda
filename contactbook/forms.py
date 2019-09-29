from django import forms

from .models import Contacto

class ContactAddForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()

class ContactAddModelForm(forms.ModelForm):
    name = forms.CharField()
    phone2 = forms.CharField(required=False)
    phone3 = forms.CharField(required=False)
    phone4 = forms.CharField(required=False)
    phone5 = forms.CharField(required=False)
    phone6 = forms.CharField(required=False)
    phone7 = forms.CharField(required=False)
    phone8 = forms.CharField(required=False)
    phone9 = forms.CharField(required=False)
    phone10 = forms.CharField(required=False)
    email2 = forms.EmailField(required=False)
    email3 = forms.EmailField(required=False)
    email4 = forms.EmailField(required=False)
    email5 = forms.EmailField(required=False)
    email6 = forms.EmailField(required=False)
    email7 = forms.EmailField(required=False)
    email8 = forms.EmailField(required=False)
    email9 = forms.EmailField(required=False)
    email10 = forms.EmailField(required=False)
    address2 = forms.CharField(required=False)
    address3 = forms.CharField(required=False)
    address4 = forms.CharField(required=False)
    address5 = forms.CharField(required=False)
    address6 = forms.CharField(required=False)
    address7 = forms.CharField(required=False)
    address8 = forms.CharField(required=False)
    address9 = forms.CharField(required=False)
    address10 = forms.CharField(required=False)
    class Meta:
        model = Contacto
        fields = ['name',
                  'phone',
                  'phone2',
                  'phone3',
                  'phone4',
                  'phone5',
                  'phone6',
                  'phone7',
                  'phone8',
                  'phone9',
                  'phone10',
                  'email',
                  'email2',
                  'email3',
                  'email4',
                  'email5',
                  'email6',
                  'email7',
                  'email8',
                  'email9',
                  'email10',
                  'address',
                  'address2',
                  'address3',
                  'address4',
                  'address5',
                  'address6',
                  'address7',
                  'address8',
                  'address9',
                  'address10']