# imports, standard library

# imports, Django core
from django.shortcuts import render
from django.shortcuts import redirect

# imports, this app
from crumbs.libs.utils import my_time
from crumbs.libs.utils import mlreader
from .forms import ExpenseForm


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            # do other things...
            try:
                expense.save()
            except:
                print("there was an error saving the form")
                pass

            return redirect('crumbs:about')
    else:
        #import requests
        #import json
        #from datetime import datetime
        #tentative = mlreader()
        #tentative_dict = json.loads(tentative.text)
        #tentative_amount = tentative_dict['extract']['AMOUNT']
        #tentative_purpose = tentative_dict['extract']['NAME']
        #tentative_date = datetime.strptime(tentative_dict['extract']['INVOICEDATE'], '%a, %d %b %Y %H:%M:%S %Z')
        #data = {
        #    'amount': tentative_amount,
        #    'purpose': tentative_purpose,
        #    'date': tentative_date,
        #}

        from datetime import datetime
        data = {
            'amount': '33',
            'date': datetime.today(),
            'purpose': 'pilfering!',
        }
        form = ExpenseForm(initial=data)

    context = {
        'title': 'Expense, create',
        'content_header': 'Expense, create',
        'form': form,
    }
    return render(request, 'crumbs/expense_create.html', context)


from django.shortcuts import get_object_or_404
from .models import Receipt
def expense_sand(request, receipt_id):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            # do other things...
            try:
                expense.save()
            except:
                print("there was an error saving the form")
                pass
            return redirect('crumbs:about')
    else:
        #receipt = get_object_or_404(Receipt, pk=4)
        context = {
            'title': 'Expense, create',
            'content_header': 'Expense, create',
        }

        if receipt_id == 0:
            print('got a macht on the receipt_id!')
            data = {
                'amount': '',
                'date': '',
                'purpose': ''
            }
            pass
        else:
            receipt = get_object_or_404(Receipt, pk=receipt_id)
            context['receipt'] = receipt
            # here invoke function to process the receipt -> mlreader()
            from datetime import datetime
            data = {
                'amount': '33',
                'date': datetime.today(),
                'purpose': 'pilfering!',
            }

        form = ExpenseForm(initial=data)
        context['form'] = form

    #context = {
    #    'title': 'Expense, create',
    #    'content_header': 'Expense, create',
    #    'form': form,
    #    'receipt': receipt,
    #}
    return render(request, 'crumbs/expense_sand.html', context)

def expense_paper(request):
    return redirect('crumbs:expense_sand', receipt_id='0')


from .models import Expense
def expense_list(request):
    expenses = Expense.objects.all()
    context = {
        'title': 'Expenses, list',
        'page_header': 'Expenses, all of them',
        'expenses': expenses,
    }
    return render(request, 'crumbs/expense_list.html', context)


def about(request):
    context = {
        'title': 'About this app',
        'page_header': 'About this app',
        'bodymessage': "About this app",
    }
    #t = my_time()
    #print(type(t))
    #print(t)
    return render(request, 'crumbs/about.html', context)


from .forms import ReceiptForm
def receipt_upload(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crumbs:about')
    else:
        form = ReceiptForm()
        context = {
            'title': 'Upload receipt',
            'page_header': 'Upload receipt',
            'form': form,
        }
    return render(request, 'crumbs/receipt_upload.html', context)


from .models import Receipt
def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        'title': 'Receipts, list',
        'page_header': 'Receipts, all of them',
        'receipts': receipts,
    }
    return render(request, 'crumbs/receipt_list.html', context)


from django.shortcuts import get_object_or_404
def receipt_read(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    context = {
        'title': 'Receipt, read',
        'page_header': 'Receipt, read',
        'receipt': receipt,
    }
    return render(request, 'crumbs/receipt_read.html', context)