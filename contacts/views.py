from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        if request.user.is_authenticated:
            has_contact = Contact.objects.filter(user_id=user_id, listing_id=listing_id)
            if has_contact:
                messages.error(request, 'Already inquried!')
                return redirect('contact')

        contact.save()

        # send mail
        send_mail(
            "Property listing inquery",
            "There has been an inquery for " + listing + "Sign into admin for more detail",
            "mahmudsajib590@gmail.com",
            [realtor_email],
            fail_silently=False
        )
        messages.success(request, 'Inquery sent realtor email.')
        

    return redirect("/")

