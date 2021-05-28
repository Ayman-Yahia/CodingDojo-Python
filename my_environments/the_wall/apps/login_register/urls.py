from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('register',views.add_new_user),
    path('login',views.login_user),
]