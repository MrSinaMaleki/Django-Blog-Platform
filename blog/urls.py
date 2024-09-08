from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),

    path('posts/', views.all_posts, name='all_posts'),

    path('authors/', views.all_authors, name='all_authors'),

    path('see_post/<int:pk>', views.one_post, name='one_post'),
    path('create_post/', views.add_new_post, name='add_new_post'),

    path('update_post/<int:pk>', views.update_post, name='update_post'),

]
