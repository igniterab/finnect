from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    profession = models.TextField(max_length=100, default="not given",null=True, blank=True)
    position = models.TextField(max_length=100, default="not given")

    about = models.TextField(max_length=100, default="not given")
    birthdate = models.DateTimeField(blank=True, null=True) 
    phone_number = models.CharField(max_length=100, default="not given")
    address = models.TextField(max_length=100, default="not given")

    facebook = models.TextField(max_length=100, default="not given")
    linkedin = models.TextField(max_length=100, default="not given")
    twitter = models.TextField(max_length=100, default="not given")
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Education(models.Model):
    institute = models.TextField(max_length=100 , default="not given")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    profile = models.ForeignKey(Profile , on_delete= models.CASCADE)

    def __str__(self):
        return self.profile.user.username +" - education at - " + self.institute

class Workexp(models.Model):
    company_name = models.TextField(max_length=100 , default="not given")
    work_descp = models.TextField(max_length=100 , default="not given")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    profile = models.ForeignKey(Profile , on_delete= models.CASCADE)
    
    def __str__(self):
        return self.profile.user.username +" - workexp at - " + self.company_name

class Projects(models.Model):
    project_name = models.TextField(max_length=100 , default="not given")
    project_descp = models.TextField(max_length=100 , default="not given")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    profile = models.ForeignKey(Profile , on_delete= models.CASCADE)

    def __str__(self):
        return self.profile.user.username +" - project - " + self.project_name

class Endorsement(models.Model):
    comment_to = models.ForeignKey(Profile , on_delete=models.CASCADE, related_name='comments')
    comment_by = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_to.user.username +" - comment by - " + self.comment_by
