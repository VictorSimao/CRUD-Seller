from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import sellersForm, AddressForm
from .models import Sellers, Address


def home(request):
    return render(request, 'home.html')


def index(request):
    data: dict = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Sellers.objects.filter(name__icontains=search)\
            or Sellers.objects.filter(cpf__icontains=search)\
            or Sellers.objects.filter(email__icontains=search)
    else:
        data['db'] = Sellers.objects.all()
        all = Sellers.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    data['index'] = sellersForm
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = sellersForm
    return render(request, 'form.html', data)


def create(request):
    form = sellersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')


def view(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    data['form'] = sellersForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data: dict = {}
    data['db'] = Sellers.objects.get(pk=pk)
    form = sellersForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('index')


def delete(request, pk):
        db = Sellers.objects.get(pk=pk)
        db.delete()
        return redirect('index')


def address(request):
    return render(request, 'address.html')


def index_address(request):
    data: dict = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Address.objects.filter(street__icontains=search)\
            or Address.objects.filter(district__icontains=search)\
            or Address.objects.filter(city__icontains=search)\
            or Address.objects.filter(state__icontains=search)
    else:
        data['db'] = Address.objects.all()
        all = Address.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    data['index_address'] = AddressForm
    return render(request, 'index_address.html', data)


def form_address(request):
    data = {}
    data['form_address'] = AddressForm
    return render(request, 'form_address.html', data)


def create_address(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_address')


def view_address(request, pk):
    data = {}
    data['db'] = Address.objects.get(pk=pk)
    return render(request, 'view_address.html', data)


def edit_address(request, pk):
    data = {}
    data['db'] = Address.objects.get(pk=pk)
    data['form_address'] = AddressForm(instance=data['db'])
    return render(request, 'form_address.html', data)


def update_address(request, pk):
    data: dict = {}
    data['db'] = Address.objects.get(pk=pk)
    form = AddressForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('index_address')


def delete_address(request, pk):
        db = Address.objects.get(pk=pk)
        db.delete()
        return redirect('index_address')