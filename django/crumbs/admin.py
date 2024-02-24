# imports, Django core
from django.contrib import admin

# imports, this app
from .models import Expense
from .models import Receipt

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'purpose', 'incurred_by')
    list_filter = ['date', 'incurred_by']

admin.site.register(Expense, ExpenseAdmin)


admin.site.register(Receipt)