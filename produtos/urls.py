from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('<int:pk>/', views.ProdutoDetailView.as_view(), name='detail'),
]