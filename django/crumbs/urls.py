# imports Django
from django.urls import path

# imports from this project
from . import views


# set the namespace for this app
app_name = 'crumbs'

urlpatterns = [
    # set the landing page for this app
    # ex: /crumbs/
    path('', views.about, name='about'),

    # ex: /crumbs/about/
    path('about/', views.about, name='about'),


    # ex: /crumbs/expense_create/
    path('expense_create/', views.expense_create, name='expense_create'),

    # ex: /crumbs/expense_sand/
    #path('expense_sand/', views.expense_sand, name='expense_sand'),
    path('expense_sand/<int:receipt_id>/', views.expense_sand, name='expense_sand'),
    path('expense_paper/', views.expense_paper, name='expense_paper'),

    # ex: /crumbs/expense_list/
    path('expense_list/', views.expense_list, name='expense_list'),


    # ex: /crumbs/receipt_list/
    path('receipt_list/', views.receipt_list, name='receipt_list'),

    # ex: /crumbs/4/
    path('receipt/<int:receipt_id>/', views.receipt_read, name='receipt_read'),

    # ex: /crumbs/receipt_upload/
    path('receipt_upload/', views.receipt_upload, name='receipt_upload'),
]