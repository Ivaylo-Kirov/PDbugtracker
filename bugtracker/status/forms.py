from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    def send_email(self):
        # send email functionality
        # https://sendgrid.com/docs/for-developers/sending-email/django/
        # api keys and such from sendgrid, EMAIL_HOST and other values added to 'settings.py' and then django import mail and mail.send_mail()
        print('sending email')
        pass