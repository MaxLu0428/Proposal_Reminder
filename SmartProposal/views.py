import os
import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Proposal, vDRM
from .forms import ProposalForm, SelectDocumentNumberForm, UploadFileForm
from difflib import HtmlDiff


def select_document_number(request):
    if request.method == 'POST':
        form = SelectDocumentNumberForm(request.POST)
        if form.is_valid():
            document_number = form.cleaned_data['document_number']
            return redirect('Proposal_list', document_number=document_number)
    else:
        form = SelectDocumentNumberForm()
    return render(request, 'Proposal_document_number.html', {'form': form})

def Proposal_list(request, document_number):
    objects = Proposal.objects.filter(document_number=document_number)
    return render(request, 'Proposal_list.html', {'objects': objects, 'document_number': document_number})

def Proposal_add(request):
    if request.method == 'POST':
        form = Proposal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Proposal_list', document_number=form.cleaned_data['document_number'])
    else:
        form = ProposalForm()
    return render(request, 'Proposal_add.html', {'form': form})

def Proposal_edit(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        form = ProposalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'redirect_url': reverse('Proposal_list', args=[obj.document_number])})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = Proposal_list(instance=obj)
    return render(request, 'Proposal_edit.html', {'form': form})

def Proposal_delete(request, pk):
    obj = get_object_or_404(Proposal, pk=pk)
    if request.method == 'POST':
        document_number = obj.document_number
        obj.delete()
        return redirect('Proposal_list', document_number=document_number)
    return render(request, 'Proposal_delete.html', {'object': obj})

def Proposal_compare(request, pk):
    obj = get_object_or_404(Proposal, pk=pk)
    comparisons = Proposal.objects.filter(name=obj.name).exclude(document_number=obj.document_number)
    differences = []
    diff = HtmlDiff()

    for comp in comparisons:
        diff_html = diff.make_file(obj.description.splitlines(), comp.description.splitlines(), fromdesc=obj.document_number, todesc=comp.document_number)
        diff_html = diff_html.replace('class="diff_add"', 'class="diff_add" style="background-color: lightblue;"')
        diff_html = diff_html.replace('class="diff_sub"', 'class="diff_sub" style="background-color: lightcoral; text-decoration: line-through;"')
        differences.append({
            'document_number': comp.document_number,
            'diff_html': diff_html
        })

    return render(request, 'Proposal_compare.html', {'obj': obj, 'differences': differences})

def upload_vdrm(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                vdrm, created = vDRM.objects.update_or_create(
                    name=row['Name'],
                    document_number=row['Document_Number'],
                    defaults={'description': row['Description']}
                )
            return JsonResponse({'message': 'vDRM data updated successfully.'})
    else:
        form = UploadFileForm()
    return render(request, 'upload_vdrm.html', {'form': form})

def vdrm_list(request):
    objects = vDRM.objects.all()
    return render(request, 'vdrm_list.html', {'objects': objects})

def update_mymodel_field(request):
    if request.method == 'POST':
        model_id = request.POST.get('id')
        field_name = request.POST.get('field')
        new_value = request.POST.get('value')

        try:
            obj = Proposal.objects.get(pk=model_id)
            setattr(obj, field_name, new_value)
            obj.save()
            return JsonResponse({'success': True})
        except Proposal.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})