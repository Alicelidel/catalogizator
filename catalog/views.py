from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from .models import Arendator
from .forms import ArendatorForm

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
    form = ArendatorForm
    return render_to_response('catalog/search_form.html', {'form': form})


def search(request):
    form = ArendatorForm(request.GET)
    person = form.data['person']
    gos_num = form.data['gos_num']
    box_num = form.data['box_num']
    auto = form.data['auto']
    registered = form.data['registered']
    ended = form.data['ended']

    boxes = Arendator.objects.filter(person__icontains=person, gos_num__icontains=gos_num,
                                     box_num__icontains=box_num, auto__icontains=auto,
                                     registered__icontains=registered, ended__icontains=ended)
    return render_to_response('catalog/box_list.html', {'boxes': boxes})