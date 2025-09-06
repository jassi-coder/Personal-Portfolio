from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(help_text="Enter percentage (0-100)")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome class e.g. fa-link")
    github_link = models.URLField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"