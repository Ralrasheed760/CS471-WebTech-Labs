
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('index2/<int:val1>/', views.index2, name='books.index2'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('one_book/', views.one_book, name='books.one_book'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
]
