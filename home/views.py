from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
# Create your views here.
def home(request):
    Project=project.objects.all().order_by('date')
    return render(request,'home.html',{'project_key':Project})
def contact(request):
    context={'page':'contact'}
    return render(request,'contact.html',context=context)
def about(request):
    Experience=experience.objects.all()
    Education=education.objects.all().order_by('-end_date')
    Achievements=achievements.objects.all()
    Certification=certifications.objects.all()
    return render(request,'about.html',{'experience_key':Experience,'education_key':Education,'Achivement_keys':Achievements,'certification_key':Certification})