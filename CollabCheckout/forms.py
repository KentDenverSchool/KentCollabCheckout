from django import forms
from CollabCheckout.models import RoomSlot

__author__ = 'Alex Clement'

class RoomSlotForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Date', 'id':'datepicker'}))
    period = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'id':'PeriodsName'}))
    room = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'id':'RoomsName'}))


    class Meta:
        model = RoomSlot
        fields = ('email', 'date', 'period', 'room')

class ManyRoomSlotForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    period = forms.CharField(max_length=256, help_text="Period:", widget=forms.TextInput(attrs={'id':'Periods'}))
    room = forms.CharField(max_length=256, help_text="Room:", widget=forms.TextInput(attrs={'id':'Rooms'}))

    class Meta:
        model = RoomSlot
        fields = ('email', 'period', 'room')