from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from .models import Arendator

def box_list(request):
    boxes = Arendator.objects.filter().order_by('box_num')
    return render(request, 'catalog/box_list.html', {'boxes': boxes})


def get_pass(request, pk):
    box = get_object_or_404(Arendator, pk=pk)
    box.get_pass()
    return render(request, 'catalog/get_pass.html', {'box': box})


def return_pass(request, pk):
    box = get_object_or_404(Arendator, pk=pk)
    box.return_pass()
    return render(request, 'catalog/return_pass.html', {'box': box})


def search_form(request):
    return render_to_response('catalog/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        boxes = Arendator.objects.filter(person__icontains=q)
        return render_to_response('catalog/box_list.html', {'boxes': boxes})

    else:
        boxes = Arendator.objects.filter().order_by('box_num')
        return render_to_response('catalog/box_list.html', {'boxes': boxes})