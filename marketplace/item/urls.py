from django.urls import path 

from . import views

app_name = 'item'

urlpatterns =[
    path('new/', views.new_item, name='new_item'),
    path('<int:item_id>/', views.detail, name='detail'),
]
