from django.shortcuts import render, redirect
from .models import About, Skill, Project, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    success = False
    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)

            # Email send (optional)
            try:
                send_mail(
                    subject=f"New Contact Message from {name}",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER ,
                    recipient_list=["rathoresonia38@gmail.com"],
                    fail_silently=False,
                )
            except:
                pass

            success = True
        else:   
            error = "Please fill all fields."

    return render(request, 'core/index.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'success': success,
        'error': error
    })
