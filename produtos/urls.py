from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]