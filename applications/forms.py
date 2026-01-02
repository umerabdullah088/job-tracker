from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    applied_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  # 👈 IMPORTANT
    )

    class Meta:
        model = JobApplication
        fields = [
            'company',
            'role',
            'status',
            'applied_date',
            'notes',
            'resume',
        ]