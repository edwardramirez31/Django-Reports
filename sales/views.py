from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Sale
# Create your views here.

def home_view(request):
    return render(request, 'sales/home.html')

class SalesListView(ListView):
    context_object_name = 'sales_list'
    template_name = 'sales/list.html'
    model = Sale
    # query: Sale.objects.all()


class SaleDetailView(DetailView):
    model = Sale
    context_object_name = 'sale'
    template_name = 'sales/detail.html'
    # query: Sale.objects.get(pk=pk)
