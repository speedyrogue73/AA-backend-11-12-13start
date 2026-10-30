from django.shortcuts import render, redirect
from .models import Amir
from .forms import CreateAmirform, UpdateAmirform, CreateUpdateAmirForm
from django.contrib import messages


def home(request):
    amirs = Amir.objects.all()
    context = {
        'amirs': amirs,
        'name': 'amirali niko',
    }
    return render(request, template_name='home/landing.html', context=context)


def detail(request, amir_id):
    amir = Amir.objects.get(id=amir_id)
    return render(request, template_name='home/detail.html', context={'amir': amir})


def create(request):
    if request.method == 'POST':
        form = CreateAmirform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            amir = Amir.objects.create(
                title=cd['title'],
                content=cd['content'],
            )
            messages.success(request, 'amir was created successfully', 'success')
            return redirect('detail', amir.id)
        else:
            messages.error(request, 'sth went wrong', 'danger')
    else:
        form = CreateAmirform()
    return render(request, template_name='home/create.html', context={'form': form})


def update(request, amir_id):
    amir = Amir.objects.get(id=amir_id)
    if request.method == 'POST':
        form = UpdateAmirform(instance=amir, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'amir was edited successfully', 'success')
            return redirect('detail', amir_id)
    else:
        form = UpdateAmirform(instance=amir)
    return render(request, template_name='home/update.html', context={'form': form})


def delete(request, amir_id):
    Amir.objects.get(id=amir_id).delete()
    messages.success(request, 'amir was deleted successfully', 'success')
    return redirect('home')
