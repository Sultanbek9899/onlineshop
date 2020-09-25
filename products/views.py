from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.views import View

# Create your views here.
from cart.forms import CartAddProductForm


class ProductListView(View):
    category_slug = None
    def get(self, request):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(status=True)
        if self.category_slug:  # есть наш слаг не пустой и пользователь выбрал какую то категорию
            category = get_object_or_404(Category, slug=self.category_slug)  # берем категории по слагу
            products = products.filter(category=category)  # берем все продукты с данной категории
        context = {
            'category': category,
            'categories': categories,
            'products': products
        }

        return render(request, 'products.html', context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id, status=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', context={'product': product,
                                                           'cart_product_form': cart_product_form
                                                           })