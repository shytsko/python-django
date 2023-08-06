from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import logging
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'lesson4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'lesson4/many_fields_form.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'lesson4/upload_image.html', {'form': form})
