from django.urls import path
from .views import (
    home_view,
    SalesListView,
    SaleDetailView,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales', SalesListView.as_view(), name='list'),
    path('sales/<int:pk>/detail', SaleDetailView.as_view(), name='sale_detail'),
]