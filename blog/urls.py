
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('see_post/<int:pk>', views.one_post, name='one_post'),
    path('create_post', views.add_new_post, name='add_new_post'),

]