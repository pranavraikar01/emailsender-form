from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject=request.POST.get('subject')
        address=request.POST.get('address')
        education=request.POST.get('education')
        contact=request.POST.get('contact')
        # Set the recipient email address
        recipient_email = email

        # Compose the email subject and body
        
        body = f"Name: {name}\nAddress:{ address}\n\nEducation qualification:{ education}\n\nContact details:{ contact}\n\nMessage: {message}"

        try:
            # Send the email
            send_mail(subject, body, email, [recipient_email], fail_silently=False)
            return render(request, 'contact/success.html')
        except Exception as e:
            error_message = str(e)
            return render(request, 'contact/error.html', {'error_message': error_message})

    return render(request, 'contact/index.html')
