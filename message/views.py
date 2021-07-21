from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from message.models import Contact


# Create your views here.
@login_required
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.info(request, 'Vous avez déjà envoyé un message')
                return redirect('message-dashboard/')

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id)
        contact.save()

        # Send email
        send_mail(
            'Property Listing contact',
            'Un message a été envoyé voir le tableau de bord',
            'academy221.py@gmail.com',
            [realtor_email, 'souleymanedialloo@yahoo.fr'],
            fail_silently=False
        )

        messages.success(request, 'Votre message a été envoyé !')
        return redirect('message-dashboard/')


@login_required
def message_contact(request):
    user_contacts = Contact.objects.order_by('-created').filter(user_id=request.user.id)
    context = {'user_contacts': user_contacts}
    return render(request, 'message/message.html', context)