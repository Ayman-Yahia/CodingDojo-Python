from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('shows',views.index1),
    path('shows/new',views.new_show),
    path('shows/create',views.show_create),
    path('shows/<int:show_id>',views.show),
    path('shows/<int:show_id>/edit',views.show_edit),
    path('shows/<int:show_id>/update',views.show_update),
    path('shows/<int:show_id>/destroy',views.destroy)
]
