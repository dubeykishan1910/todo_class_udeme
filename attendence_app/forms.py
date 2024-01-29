# attendance_app/forms.py
from django import forms

class AttendanceForm(forms.Form):
    entry_time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    exit_time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}), required=False)
