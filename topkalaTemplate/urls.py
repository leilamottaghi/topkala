
from django.urls import path
from . import views

app_name = 'topkalaTemplate'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<int:product_id>/', views.SingleProductView.as_view(), name='single-product'),
    path('product/<int:product_id>/add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('product/<int:product_id>/send-email/', views.send_product_email, name='send_product_email'),
    path('product/sent-success/', views.ProductSentSuccessView.as_view(), name='product_sent_success'),
    path('product/sent-fail/', views.ProductSentFailView.as_view(), name='product_sent_fail'),
    # path('product/<int:product_id>/add_to_favorite/', views.AddToFavoriteView.as_view(), name='add_to_favorite'),
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart-empty/', views.CartEmptyView.as_view(), name='cart-empty'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('404/', views.PageNotFoundView.as_view(), name='404'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('profile-additional-info/', views.ProfileAdditionalInfoView.as_view(), name='profile-additional-info'),
    path('profile-favorites/', views.ProfileFavoritesView.as_view(), name='profile-favorites'),
    path('profile-orders-return/', views.ProfileOrdersReturnView.as_view(), name='profile-orders-return'),
    path('profile-personal-info/', views.ProfilePersonalInfoView.as_view(), name='profile-personal-info'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('search-amazing/', views.SearchAmazingView.as_view(), name='search-amazing'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('shopping-complete-buy/', views.ShoppingCompleteBuyView.as_view(), name='shopping-complete-buy'),
    path('shopping-no-complete-buy/', views.ShoppingNoCompleteBuyView.as_view(), name='shopping-no-complete-buy'),
    path('shopping-payment/', views.ShoppingPaymentView.as_view(), name='shopping-payment'),
    path('shopping/', views.ShoppingView.as_view(), name='shopping'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]
