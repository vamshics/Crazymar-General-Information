from django.db import models
#from django.db.models import CharField
# Create your models here.
class JobCre(models.Model):
    jobtitle = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Position = models.CharField(max_length=20)
    Experience = models.CharField(max_length=20)
    NoOfVacancy = models.IntegerField()
    Package = models.CharField(max_length=20)
    CompanyLogo = models.FileField(upload_to='images')
    JobType = models.CharField(max_length=20)
    MinQualification = models.CharField(max_length=60)
    Skills = models.CharField(max_length=60)
    maill1 = models.EmailField()
    phoneNo = models.IntegerField()
    landline = models.IntegerField()
    website = models.CharField(max_length=50)
    addresss = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    fb = models.CharField(max_length=20)
    ggleplus2 = models.CharField(max_length=20)
    twitter = models.CharField(max_length=20)
    linkedin1 = models.CharField(max_length=20)
    pininterest1 = models.CharField(max_length=20)
    instagramm = models.CharField(max_length=20)

    def __str__(self):
        return self.jobtitle