from django.urls import path
from .views import home,articles,showdetails,addpost,deleteview,editview

urlpatterns = [
    path('',home,name="home"),
    path('articles', articles.as_view()   ,name="articles"),
    path('details/<int:pk>', showdetails.as_view(), name='details'),
    path('newpost',addpost.as_view(), name="+post"),
    path('edit/<int:pk>',editview.as_view(), name='edit'),
    path('delete/<int:pk>',deleteview.as_view(), name='delete'),
]