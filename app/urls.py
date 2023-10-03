from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Index,name="index"),
    path('product-detail/<slug:pk>',views.ProductDetail.as_view(),name="product-detail"),
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('profile/',views.ProfilePage,name="Profile"),
    path('address/',views.AddressPage,name="Address"),
    path('updateaddress/<int:pk>',views.UpdatePage,name="UpdateAddress"),

    # Login authentication
    path('registration/',views.SignupPage,name="signup"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.Logout,name="Logout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)