from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Sale
from .forms import SalesForm
# Create your views here.

def home_view(request):
    form = SalesForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)
        
    context = {
        'form': form,
    }
    return render(request, 'sales/home.html', context)

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
