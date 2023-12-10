from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category
from .forms import RecordsForm

# Create your views here.


def index(request):
    categories = Category.objects.all()
    # print(categories)
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
