from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('dojo',views.add_Dojo),
    path('ninja',views.add_Ninja),
    path('delete',views.delete_dojo)
]
