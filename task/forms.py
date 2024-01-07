from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, label='Title', required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}),label='Body')