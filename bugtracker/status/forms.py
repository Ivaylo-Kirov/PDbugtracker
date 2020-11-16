from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    def send_email(self):
        # send email functionality
        print('sending email')
        pass