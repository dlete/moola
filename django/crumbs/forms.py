# imports, Django core
from django.forms import ModelForm
from django.forms import DateInput, FileInput, NumberInput, TextInput

# imports, this app
from crumbs.models import Expense


class ExpenseForm(ModelForm):

    class Meta:
        model = Expense
        fields = ['amount', 'date', 'purpose',]

        # CSS styling in Django forms
        # https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
        widgets = {
            'amount': NumberInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'purpose': TextInput(attrs={'class': 'form-control'}),
        }


# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
from crumbs.models import Receipt
class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['receipt',]
        widgets = {
            'receipt': FileInput(attrs={'class': 'custom-file-input'}),
        }
        # https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name
        labels = {
            'receipt': 'Please select file to upload',
        }