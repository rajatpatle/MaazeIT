from django.shortcuts import render, HttpResponse,redirect
from .forms import ManageForm
from .models import Management
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='log_url')
def addEmp(request):
    form = ManageForm()
    template_name = 'Crud_app/add.html'
    if request.method == 'POST':
        form = ManageForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='log_url')
def showEmp(request):
    data = Management.objects.all()
    template_name = 'Crud_app/show.html'
    context = {'data':data}
    return render(request, template_name, context)
    
def updateEmp(request, pk):
    obj = Management.objects.get(id=pk)
    form = ManageForm(instance=obj)
    template_name = 'Crud_app/add.html'
    if request.method == 'POST':
        form = ManageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def deleteEmp(request, pk):
    obj = Management.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'Crud_app/confirm.html'
    context = {'data': obj}
    return render(request, template_name, context)
