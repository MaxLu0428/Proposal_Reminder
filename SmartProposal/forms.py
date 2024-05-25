from django import forms
from .models import Proposal,vDRM

class ProposalForm(forms.ModelForm):
    class Meta:
        model=Proposal
        fields = ['Name',"Description","Document_Number"]

class SelectDRMForm(forms.Form):
    DRM= forms.ChoiceField(choices=[])

    def __init__(self,*args,**kwargs):
        super(SelectDRMForm,self).__init__(*args,**kwargs)
        self.fields['DRM'].choices=[(drm,drm) for drm in Proposal.objects.values_list('Document_Number',flat=True).distinct()]

class UploadFileForm(forms.Form):
    file = forms.FileField()
    