from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import uploadimg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# create views


def index(request):
    list = uploadimg.objects.all().order_by('-usr_date')
# This statement ensures there is ordering of pics as per the date uploaded which is taken under models.py
    paginator = Paginator(list, 10)
# Shows 10 list of images and descriptions per page

    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
# If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
# If page is out of range (e.g. 100), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return render(request, 'Rigapp/form.html', {'list':list})


def imgupload(request):
    if request.method == 'POST':
        forma = DocumentForm(request.POST, request.FILES)
        if forma.is_valid():
            data = uploadimg()
            data.usr_image = forma.cleaned_data['usr_image']
            data.description = forma.cleaned_data['description']
            forma.save()
            print ('validated')
# prints to check whether the loop is entered or not in terminal
            return redirect('/Rigapp/')
        else:
            print ('not validated')
# prints to check whether the loop is entered or not in terminal. Enables better understanding if there is an error.
            forma = DocumentForm()
        return render(request, 'Rigapp/form.html')
