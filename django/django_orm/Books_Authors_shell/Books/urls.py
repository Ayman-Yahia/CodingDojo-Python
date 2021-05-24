from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('add_book',views.add_book),
    path('books/<int:book_id>',views.book_desc),
    path('add_author_to_book',views.add_author_to_book),
    path('authors',views.index1),
    path('add_author',views.add_author),
    path('authors/<int:author_id>',views.author_desc),
    path('add_book_to_author',views.add_book_to_author)
]
