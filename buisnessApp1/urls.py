from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('blogs/', views.blogs),
    path('products/', views.products),
    path('feedback/', views.feedback),
    path('blogs/blogContent/<int:id>', views.blogContent, name='blogContent'),
    path('products/productContent/<int:id>', views.productContent, name='productContent')
]