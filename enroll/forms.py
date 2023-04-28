
from django import forms
from .models import User
class StudentRegisteration(forms.ModelForm):

    
    
    class Meta:
        
        model=User
        fields=['name','email','Address','father_Name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            #'Ph_No':forms.NumberInput(attrs={'class':'form-control'}),
            'father_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            #'Resume':forms.FileInput(attrs={'class':'form-control'}),

        }
