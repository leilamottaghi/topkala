from django.views.generic import View
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import EmailProductLinkForm
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse




class AddCommentView(View):
    # @login_required
    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        print("aaaaaaaaaaaaa",request.user)
        author = request.user
        text = request.POST['text']
        parent_comment_id = request.POST.get('parent_comment_id')  # دریافت شناسه نظر والد اگر وجود داشته باشد
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
            Comment.objects.create(product=product, author=author, text=text, parent_comment=parent_comment)
        else:
            Comment.objects.create(product=product, author=author, text=text)
            
        return redirect('topkalaTemplate:single-product', product_id=product_id)




class ProductSentSuccessView(View):
    def get(self, request):
        return HttpResponse('ارسال محصول موفقیت‌آمیز بود!')


class ProductSentFailView(View):
    def get(self, request):
        return HttpResponse('ارسال محصول ناموفق بود!')



def send_product_email(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        email_form = EmailProductLinkForm(request.POST)
        if email_form.is_valid():
            to_email = email_form.cleaned_data['to_email']
            
            # ایجاد لینک محصول
            product_url = request.build_absolute_uri(product.get_absolute_url())

            # ارسال ایمیل
            subject = f'لینک محصول: {product.title}'
            message = f'لینک محصول: {product_url}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [to_email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            # موفقیت‌آمیز بودن ارسال ایمیل را به کاربر نمایش دهید
            return redirect('topkalaTemplate:product_sent_success')
    
    # در صورتی که ارسال ایمیل موفقیت‌آمیز نبود
    return redirect('topkalaTemplate:product_sent_fail')




# @login_required  # تأكید می‌کند که کاربر وارد شده باشد.
def add_to_favorites(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        favorite, created = FavoriteProduct.objects.get_or_create(user=request.user, product=product)
        if created:
            return JsonResponse({'status': 'added'})
        else:
            return JsonResponse({'status': 'already_added'})
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'محصول مورد نظر یافت نشد'})



class SingleProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        categories = []

        categories.append(product.category)

        parent_category = product.category.parent
        while parent_category:
            categories.append(parent_category)
            parent_category = parent_category.parent

        email_form = EmailProductLinkForm()

        brand = product.brand 

        comments = Comment.objects.filter(product=product)
        
        context = {
            'product': product,
            'categories': reversed(categories), 
            'email_form': email_form,
            'brand': brand,
            'comments': comments,
        }

        return render(request, 'topkalaTemplate/single-product.html', context)




class IndexView(View):
    def get(self, request):
        slider_images = SliderImage.objects.all()
        products = Product.objects.filter(
            Q(category__title="شگفت‌انگیزها") | Q(category__parent__title="شگفت‌انگیزها")
        )
        category1 = Category.objects.get(title='kkkk')
        category2 = Category.objects.get(title='کالای دیجیتال')

        products_category1 = Product.objects.filter(category=category1)
        products_category2 = Product.objects.filter(category=category2)

        special_brands = SpecialBrand.objects.all()

        recent_discounted_products = Product.objects.filter(discount_percent__gt=0).order_by('-id')[:4]

        context = {
            'products': products,
            'slider_images': slider_images,
            'category1':category1,
            'category2':category2,
            'products_category1': products_category1,
            'products_category2': products_category2,
            'special_brands': special_brands,
            'recent_discounted_products': recent_discounted_products,

        }

        return render(request, 'topkalaTemplate/index.html', context)





class AboutView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/about.html', {})

class CartView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/cart.html', {})

class CartEmptyView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/cart-empty.html', {})

class CheckoutView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/checkout.html', {})

class PageNotFoundView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/404.html', {})

class LoginView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/login.html', {})

class PasswordChangeView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/password-change.html', {})

class ProfileAdditionalInfoView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/profile-additional-info.html', {})

class ProfileFavoritesView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/profile-favorites.html', {})

class ProfileOrdersReturnView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/profile-orders-return.html', {})

class ProfilePersonalInfoView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/profile-personal-info.html', {})

class ProfileView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/profile.html', {})

class RegisterView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/register.html', {})

class SearchAmazingView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/search-amazing.html', {})

class SearchView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/search.html', {})

class ShoppingCompleteBuyView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/shopping-complete-buy.html', {})

class ShoppingNoCompleteBuyView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/shopping-no-complete-buy.html', {})

class ShoppingPaymentView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/shopping-payment.html', {})

class ShoppingView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/shopping.html', {})

class WelcomeView(View):
    def get(self, request):
        return render(request, 'topkalaTemplate/welcome.html', {})
