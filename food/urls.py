from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
	#path('', views.index, name='index'),
	#below is the replacement for above line
	path('', views.IndexClassView.as_view(), name='index'),
	path('item', views.item, name='item'),
	#path('<int:item_id>/', views.detail, name='detail'),
	path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
	#path('addItem/', views.addItem, name='addItem'),
	path('addItem/', views.AddItem.as_view(), name='addItem'),
	path('updateItem/<int:id>/', views.updateItem, name='updateItem'),
	path('deleteItem/<int:id>/', views.deleteItem,name='deleteItem'),
	
]