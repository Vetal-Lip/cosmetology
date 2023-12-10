from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Procedure
from .forms import RecordsForm

# Create your views here.


def index(request):
    categories = Category.objects.all()
    # massage = Category.objects.get(pk=1)
    # print(massage.procedures.all())
    # for p in procedures:
    #     print(p.cat.name_service)
    return render(request, 'main/services.html', {'categories': categories})


def about(request):
    return render(request, 'main/about.html')


def record(request):
    error = ''
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    categories = Category.objects.all()
    form = RecordsForm()

    data = {
        'categories': categories,
        'form': form,
        'error': error
    }

    return render(request, 'main/record.html', data)

def show_category(request, category_id):
    categories = Category.objects.all()
    description = Category.objects.get(pk=category_id).about_service
    cat = Category.objects.get(pk=category_id)
    procedure = cat.procedures.all()
    id = category_id
    print(category_id)
    data = {
        'categories': categories,
        'procedures':procedure,
        'description':description,
        'id':id,
        
    }
    return render(request, 'main/procedures.html', data)