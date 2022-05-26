from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view()),
    path('todos/<str:pk>/',views.DetailView.as_view()),
    path('create/',views.CreateView.as_view()),
    path('update/<str:pk>/',views.UpdateView.as_view()),
    path('delete/<str:pk>/',views.DeleteView.as_view())

]