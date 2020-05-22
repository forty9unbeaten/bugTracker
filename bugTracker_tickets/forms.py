from django import forms
from bugTracker_tickets.models import BugTicket


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ['title', 'description', 'creator']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 15})
        }


class TicketDetailForm(NewTicketForm):
    assign = forms.BooleanField(
        label='Assign to me', required=False, widget=forms.CheckboxInput)
    completed = forms.BooleanField(
        label='Mark as Completed', required=False, widget=forms.CheckboxInput)
    invalid = forms.BooleanField(
        label='Mark as Invalid', required=False, widget=forms.CheckboxInput)
