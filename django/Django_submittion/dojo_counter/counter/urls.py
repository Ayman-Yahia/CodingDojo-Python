from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('add',views.add),
    path('destroy_session',views.destroy)
]
