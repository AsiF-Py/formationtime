from django.shortcuts import render,redirect
from .models import Document,Invoice,Support
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def document_list(request):
    document_list = Document.objects.filter(user=request.user)
    return render(request,'document/document_list.html',{'document_list':document_list})
@login_required()
def invoice_list(request):
    invoice_list = Invoice.objects.filter(user=request.user)
    return render(request,'document/invoice_list.html',{'invoice_list':invoice_list})

@login_required()
def support(request):
    support = Support.objects.filter(user=request.user)
    return render(request,'document/support.html',{'support':support})

@login_required()
def create_support(request):
    if request.method == 'POST':
        problem = request.POST.get('problem')
        title = request.POST.get('title')
        Support.objects.create(user=request.user,problem=problem,title=title)
        return redirect('support')
    return render(request,'document/create_support.html',{'support':support})
