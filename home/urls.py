from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('about', views.inputAbout, name="about"),
    path('contact', views.inputContact, name="contact"),
    # Для работы со статьями - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    path('news', views.ShowNewsView.as_view(), name='news'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
]
