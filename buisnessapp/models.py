from django.db import models

# Create your models here.
class userregister(models.Model):
    Name=models.CharField(max_length=30)
    EmailID=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Mobile=models.BigIntegerField()
    AdharNo=models.CharField(max_length=30)
    UserType=models.CharField(max_length=30)
class businessproposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    Name=models.CharField(max_length=30,default='default')
    BName=models.CharField(max_length=30)
    CRegNo=models.IntegerField()
    Category=models.CharField(max_length=30)
    Objective=models.TextField()
    Lifetime=models.TextField()
    Experience=models.CharField(max_length=30)
    SkillSet=models.CharField(max_length=100)
    ContactNo=models.BigIntegerField()
    Address=models.TextField()
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return self.Name
class query(models.Model):
    Name=models.CharField(max_length=30)
    Query=models.TextField()
    Reply=models.TextField(default='Pending your query reply')
    def __str__(self):
        return self.Name
class appliedjobs(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('you can attend interview', 'Accepted'),
        ('Rejected', 'Declined'),
    ]
    BusinessMan=models.CharField(max_length=30)
    Business=models.CharField(max_length=30)
    Applicant=models.CharField(max_length=30)
    NoticePeriod=models.CharField(max_length=30)
    ExpectedSalary=models.IntegerField()
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending your application')
class interestedinvestor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined your interest', 'Declined'),
    ]
    BusinessMan=models.CharField(max_length=30)
    Business=models.CharField(max_length=30)
    Applicant=models.CharField(max_length=30)
    InvestmentType=models.CharField(max_length=30)
    Amount=models.IntegerField()
    TimeofInvestment=models.CharField(max_length=30)
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending your interest')
class contact(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Message=models.TextField()
    def __str__(self):
        return self.Name





    