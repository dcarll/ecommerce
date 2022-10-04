from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Produto

# Create your views here.

class ProdutoListView(ListView):

    #pega todos os objetos ptodutos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()
    template_name = 'produtos/list.html'
    model = 'Produto'
    context_object_name = 'produtos'

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
        return context
'''
#FBV function based view
def produto_list_view(request):
    queryset = Produto.objects.all()
    context = {
        'produtos': queryset
    }

    return render(request, 'produtos/list.html', context)
'''

#class based view para trazer os detalhes de um determinado produto
class ProdutoDetailView(DetailView):
	'''Mostra os detalhes de um produto'''
	model = Produto
	template_name = 'produtos/detalhes.html'
	context_object_name = 'produto'


#function based view para trazer os detelhes de um determinado produto
def produto_detail_view(request):
    context = Produto.objects.all()
    return render(request, 'produtos/detalhes.html', context)