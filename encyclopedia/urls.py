from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entrypage, name="entry page"),
    path("new", views.new, name="new"),
    path('edit/<str:title>', views.edit, name="edit"),
    path('edit', views.confirm_edit, name='confirm_edit'),
    path('random', views.random_entry, name="random")
]
