from django import forms

class EmailProductLinkForm(forms.Form):
    to_email = forms.EmailField(label='آدرس ایمیل مخاطب', required=True)
