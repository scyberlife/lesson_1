from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
    # queryset = models.Product.objects.filter().order_by('-id')
    queryset = models.ProductCL.objects.filter(tag__name="игры")

    template_name = "products/product_list.html"

    def get_queryset(self):
            return models.ProductCL.objects.filter(tag__name="игры")


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)