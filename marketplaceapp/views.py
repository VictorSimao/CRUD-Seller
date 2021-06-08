from django.shortcuts import redirect, render
from .models import Marketplace, ConfigMarketplace


def index(request):
    if request.path == "/marketplace/":
        models = Marketplace.objects.all()
        return render(request, "marketplace.html", {'model': models})
    elif request.path == "/marketplace/configs/":
        models = ConfigMarketplace.objects.all()
        return render(request, "config.html", {'model': models})
    return render(request, "marketplace.html")

def form(request):
    if request.path == "/marketplace/form/":
        data = request.GET
        if data.get('id'):
            model = Marketplace.objects.get(id = request.GET['id'])
            return render(request, "marketplace_form.html", {'data': model})
        return render(request, "marketplace_form.html")
    elif request.path == "/marketplace/configs/form/":
        data = request.GET
        marketplaces = Marketplace.objects.all()
        if data.get('id'):
            model = ConfigMarketplace.objects.get(id = request.GET['id'])
            return render(request, "config_form.html", {'data': model}, {'data_market': marketplaces})
        return render(request, "config_form.html", {'data_market': marketplaces})

def save(request):
    if request.path == "/marketplace/save/":
        data = request.GET
        if data.get('id'):
            model = Marketplace.objects.get(id = data['id'])
            model.name = data['name']
            model.description = data['description']
            model.save()
        else:
            create = Marketplace(name=data['name'])
            create.save()
    elif request.path == "/marketplace/configs/form/save/":
        data = request.GET
        if data.get('id'):
            model = ConfigMarketplace.objects.get(id = data['id'])
            model.apis = data['apis']
            model.keys = data['keys']
            model.endpoints = data['endpoints']
            model.save()
        else:
            marketplace = Marketplace.objects.get(id = data['marketplace'])
            create = ConfigMarketplace(
                apis = data['apis'],
                keys = data['keys'],
                endpoints = data['endpoints'],
                marketplace = marketplace
            )
            create.save()
        return redirect('/marketplace/configs/')
    return redirect('/marketplace/')

def delete(request):
    if request.path == "/marketplace/delete/":
        data = request.GET
        model = Marketplace.objects.get(id = data['id'])
        model.delete()
    elif request.path == "/marketplace/configs/delete/":
        data = request.GET
        model = ConfigMarketplace.objects.get(id = data['id'])
        model.delete()
        return redirect('/marketplace/configs/')
    return redirect('/marketplace/')
