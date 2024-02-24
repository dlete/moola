# imports Django
from django.urls import path

# imports from this project
from . import views


# set the namespace for this app
app_name = 'people'

urlpatterns = [
    # set the landing page for this app
    # ex: /core/
    path('', views.about, name='about'),

    # ex: /people/about/
    path('about/', views.about, name='about'),
]
