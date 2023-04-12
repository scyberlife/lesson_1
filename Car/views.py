from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .forms import CommentForm, CarForm
from .models import CarShop, CommentPeople
from django.urls import reverse_lazy, reverse


def car_list_view(request):
    car_object = models.CarShop.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


# def car_detail_view(request, id):
#     car_detail = get_object_or_404(models.CarShop, id=id)
#     return render(request, 'car_detail.html', {'car_detail': car_detail})

class CarDetailView(DetailView):
    model = CarShop
    template_name = 'car_detail.html'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return get_object_or_404(CarShop, id=obj.id)
class CarListView(ListView):
    template_name = "car_list.html"
    queryset = models.CarShop.objects.all()
    def get_queryset(self):
        return models.CarShop.objects.all()

class CreateCarView(CreateView):
    template_name = 'add_car.html'
    form_class = forms.CarForm
    queryset = models.CarShop.objects.all()
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCarView, self).form_valid(form=form)

# def add_car_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>complete</h2>')
#     else:
#         form = forms.CarForm()
#     return render(request, 'add_car.html', {'form': form})


# def update_car(request, id):
#     show = get_object_or_404(models.CarShop, id=id)
#     if request.method == 'POST':
#         form = forms.CarForm(instance=show, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>complete</h2>')
#     else:
#         form = forms.CarForm(instance=show)
#     return render(request, 'update_car.html', {'form': form, 'object': show})


class UpdateCarView(UpdateView):
    model = models.CarShop
    form_class = CarForm
    template_name = 'update_car.html'
    success_url = reverse_lazy('car_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

# def delete_car(request, id):
#     car_object = get_object_or_404(models.CarShop, id=id)
#     car_object.delete()
#     return HttpResponse('<h2>complete</h2>')

class DeleteCarView(DeleteView):
    model = models.CarShop
    template_name = 'carshop_confirm_delete.html'
    success_url = reverse_lazy('car_list')
    def delete(self, request, *args, **kwargs):
        car_object = self.get_object()
        car_object.delete()
        return HttpResponse('<h2>complete</h2>')

def get_object(self, **kwargs):
    car_detail = self.kwargs.get('id')
    return get_object_or_404(models.CarShop, id=car_detail)


# def add_comment(request, id):
#     car_shop = get_object_or_404(CarShop, id=id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.car_shop = car_shop
#             comment.save()
#         return redirect('car_detail', id=id)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment.html', {'form': form})

class AddCommentView(CreateView):
    model = CommentPeople
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        car_shop = get_object_or_404(CarShop, pk=self.kwargs['pk'])
        form.instance.car_shop = car_shop
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.kwargs['pk']})

class Search(ListView):
    template_name = "car_list.html"
    context_object_name = 'car'
    paginate_by = 5

    def get_queryset(self):
        return models.CarShop.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context