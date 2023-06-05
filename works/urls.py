from django.urls import path
from .views import works, works_single

app_name = 'works_app'

urlpatterns = [
    path('works/', works, name='works'),
    path('single/', works_single, name='single'),
]