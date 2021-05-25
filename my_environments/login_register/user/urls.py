from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('new_user',views.add_new_user),
    path('login',views.login_user)
]