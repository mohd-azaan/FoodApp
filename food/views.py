from django.shortcuts import render, redirect 
from .models import Items
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    context = {
        'item_list': Items.objects.all()
    }
    return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    model = Items
    template_name = 'food/index.html'
    context_object_name = 'item_list'





def item(request):
    return render(request, 'food/item.html')





def detail(request, item_id):
    item = Items.objects.get(id=item_id)
    print(item)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)

class FoodDetail(DetailView):
    model = Items
    template_name = 'food/detail.html'





def addItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})


class AddItem(CreateView):
    model = Items
    template_name = 'food/item-form.html'
    fields = ['item_name', 'item_description', 'item_price', 'item_image']

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)





def updateItem(request, id):
    item = Items.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def deleteItem(request, id):
    item = Items.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete-item.html', {'item': item})

