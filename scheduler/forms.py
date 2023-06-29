from django import forms
from .models import Workstation, Schedule


class WorkstationForm(forms.ModelForm):
    class Meta:
        model = Workstation
        fields = '__all__'  # Or specify the fields you want to include


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'  # Or specify the fields you want to include
