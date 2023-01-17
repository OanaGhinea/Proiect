from django.urls import path
from .views import HomeView, ArticoleDetailView, AdaugaPostareView, EditarePostareView, StergerePostareView, AdaugaTipuriView, TipuriView
    #, LikeView


# from . import views
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('articol/<int:pk>', ArticoleDetailView.as_view(), name='articole_details'),
    path('adauga_postare/', AdaugaPostareView.as_view(), name='adauga_postare'),
    path('adauga_tipuri/', AdaugaTipuriView.as_view(), name='adauga_tipuri'),
    path('articol/editare_postare/<int:pk>', EditarePostareView.as_view(), name='editare_postare'),
    path('articol/<int:pk>/sterge', StergerePostareView.as_view(), name='stergere_postare'),
    path('tipuri/<str:tip>/', TipuriView, name='tipuri'),
    # path('like/<int:pk>',LikeView, name='like_blog'),


]