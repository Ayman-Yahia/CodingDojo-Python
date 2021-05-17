from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('process_money', views.process),
    path('reset', views.reset)
]
