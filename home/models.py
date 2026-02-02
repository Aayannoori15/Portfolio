from django.db import models

# Create your models here.
class experience(models.Model):
    company_name=models.CharField(max_length=100)
    domain=models.CharField(max_length=100,null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    location=models.CharField(max_length=100)
    images=models.ImageField()
    description=models.TextField()
    def __str__(self):
        return self.company_name
class education(models.Model):
    institute_name=models.CharField(max_length=100)
    course=models.CharField(max_length=100,null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    location=models.CharField(max_length=100)
    images=models.ImageField()
    description=models.TextField()
    def __str__(self):
        return self.institute_name
class project(models.Model):
    project_name=models.CharField(max_length=100)
    date=models.DateField()
    image=models.ImageField()
    description=models.TextField()
    techstack=models.TextField()
    link=models.URLField()
    def __str__(self):
        return self.project_name
class achievements(models.Model):
    event_name=models.CharField(max_length=100)
    date=models.DateField()
    image=models.ImageField()
    description=models.TextField() 
    def __str__(self):
        return self.event_name
class certifications(models.Model):
    certificate_name=models.CharField(max_length=100)
    issue_date=models.DateField()
    images=models.ImageField()
    description=models.TextField()
    link=models.URLField()
    def __str__(self):
        return self.certificate_name