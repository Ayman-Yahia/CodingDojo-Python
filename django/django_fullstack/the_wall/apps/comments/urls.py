from django.urls import path
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('add_message',views.add_message),
    path('add_comment',views.add_comment),
    path('delete_com/<int:com_id>',views.deletecom),
    path('delete_msg/<int:msg_id>',views.deletemsg),
    path('log_out',views.logout)
]
