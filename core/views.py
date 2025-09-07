from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import About, Skill, Project

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Optional email
            try:
                send_mail(
                    subject=f"New Contact Message from {contact.name}",
                    message=contact.message,
                    from_email='singh.jaspreet2003@gmail.com',
                    recipient_list=["rathoresonia38@gmail.com"],
                    fail_silently=True,
                )
            except:
                pass

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': '✅ Message sent successfully!'})
            messages.success(request, '✅ Message sent successfully!')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': '❌ Please correct the errors below!'})
            messages.error(request, '❌ Please correct the errors below.')

    return render(request, "core/index.html", {
        "about": about,
        "skills": skills,
        "projects": projects,
        "form": form,
    })
