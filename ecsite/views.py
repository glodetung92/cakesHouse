from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, CartItem



class HomeView(TemplateView):
	template_name = 'ecsite/home.html'


class ProductListView(ListView):
	model = Product
	template_name = 'ecsite/list.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		product = Product.objects.all()
		context['cakes'] = Product.objects.filter(type='cakes')
		context['bakedcakes'] = Product.objects.filter(type='bakedcakes')
		context['goods'] = Product.objects.filter(type='goods')
		return context


class ProductDetailView(DetailView):
	model = Product
	template_name = 'ecsite/detail.html'
	content_object_name = 'product'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_anonymous:
			pass
		else:
			user = self.request.user
			mycartitem = (CartItem.objects.filter(user_id=user)).values_list('product_id')
			context['cart_contents'] = Product.objects.filter(id__in=mycartitem)
		return context


class CartView(ListView):
	model = CartItem
	template_name = 'ecsite/cart.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		cartitem = CartItem.objects.filter(user=user)
		if len(cartitem) > 0:
			# check product is isset on cart
			product = CartItem.objects.filter(product=kwargs['product'])
		else:
			cartitem = CartItem(qty=1, user=user, product
