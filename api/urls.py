from django.urls import path

from api import views

urlpatterns = [
    path("books/", views.BookListView.as_view(), name="books")
]
