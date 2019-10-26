from django.urls import path

from .views import homePageView, pageCountView

urlpatterns = [
    path('', homePageView, name='home'),
    path('counts/', pageCountView, name='counts')
]