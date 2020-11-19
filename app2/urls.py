from django.urls import path
from app2 import views
app_name ='app2'

urlpatterns = [
    path('func2/', views.func2, name='func2')
]