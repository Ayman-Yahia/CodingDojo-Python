from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('register',views.add_new_user),
    path('login',views.login_user),
    path('books',views.books),
    path('fav_books',views.add_book),
    path('books/<int:book_id>',views.book_show),
    path('books/update/<int:book_id>',views.update_book),
    path('books/delete/<int:book_id>',views.delete_book),
    path('books/fav_book/<int:book_id>',views.fav_book),
    path('books/un_fav/<int:book_id>',views.un_fav),
    path('log_out',views.log_out)
]