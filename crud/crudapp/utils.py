from django.core.mail import send_mail,EmailMessage
# from django.Http import HttpResponse
# Your view or function
def send_email_v(request):
    subject = 'Subject of the email'
    message = 'this message was sent by django.'
    from_email = 'mangeshsathe1353@gmail.com'  # Sender's email address
    recipient_list = ['mangeshsathe2003@gmail.com']  # Recipient's email address

    send_mail(subject, message, from_email, recipient_list)

    # Optionally, you can redirect to a success page or return a response
    # return HttpResponse ('Email sent successfully!')
    
