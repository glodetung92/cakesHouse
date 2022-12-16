from django.urls import path

from .views import HomeView, ProductListView, ProductDetailView, CartView

app_name = 'ecsite'
urlpatterns = [
	path('home/', HomeView.as_view(), name='home'),
	path('list/', ProductListView.as_view(), name='product_list'),
	path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
	path('cart/', CartView.as_view(), name='cart'),
]
