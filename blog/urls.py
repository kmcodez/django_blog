from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.index, name='index'),
    # path('post/detail', views.detail, name='detail'),
    path("post/<int:post_id>", views.detail_int, name="int_detail"),  # this is dynamic url which can be changed
    path("post/<str:post_id>", views.detail_str, name="str_detail"),  # this is dynamic url which can be changed

    # when redirects given should in old one return redirect(newly given url path), here now given "new_url"
    # should be given as a string of exeact new url path
    path("new_url", views.new_url_view, name="new_url"),
    path("old_url", views.old_url_redirect, name="old_url"),

    # when changes the url path any cases in future, we do change all the given places
    # so that work minimize that do reverse name to change the url path
    path("new_reverse_url", views.redirect_new_url, name="new_page_url"),
    path("old_page_url", views.redirect_old_url, name="old_page_url"),

    path("", views.front_index, name="front_index"),
    # path("front/<str:post_id>", views.front_detail, name="front_detail"),
    path("front/<str:slug>", views.front_detail, name="front_detail"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_view, name="about")
]
