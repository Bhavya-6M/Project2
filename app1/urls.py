

from django.urls import path
from app1 import views
app_name = 'app1'

urlpatterns = [
    path('func1/', views.func1, name='func1')
]