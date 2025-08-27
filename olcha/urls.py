from django.urls import path,include
from olcha.views import CategoryListAPIView,SubcategoryListAPIView, ProductListAPIView,ProductDetailAPIView

urlpatterns = [
    path('',CategoryListAPIView.as_view(),),
    path('category/<slug:parent_slug>/',SubcategoryListAPIView.as_view()),
    path("products/", ProductListAPIView.as_view()),
    path("products/<int:id>/", ProductDetailAPIView.as_view()),
]
