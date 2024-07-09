from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:id> ", views.listin, name="listing"),
    path("watchlist", views.watch, name="watch"),
    path("removed", views.notwatch, name="notwatch"),
    path("bid", views.biding, name="bid"),
    path("close", views.close, name="close"),
    path("comment", views.comment, name="comment"),
    path("category", views.category, name="category"),
    path("<str:cat>", views.categories, name="cat"),
    path('accounts/login/', views.login_view, name="required")
]
