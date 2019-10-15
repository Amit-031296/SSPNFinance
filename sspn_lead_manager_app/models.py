from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class AllLeads(models.Model):
    product_type_choices=(('Micro Finance','Micro Finance'),
                        ('Instant Salary','Instant Salary'),
                        ('Consumer Finance','Consumer Finance'))
    status_type_choices=(('All Status','All Status'),
                        ('Pending Status','Pending Status'),
                        ('In Process Status','In Process Status'),
                        ('Approved Status','Approved Status'),
                        ('Rejected Status','Rejected Status'))
    def sr_number_genrator():
        latest_object = AllLeads.objects.latest('date_of_entry')
        latest_sr_no = latest_object.sr_no
        if latest_object == None:
            return 1
        else:
            return (latest_sr_no+1)
    sr_no = models.IntegerField(default=sr_number_genrator)
    full_name = models.CharField(max_length=920)
    gender = models.CharField(max_length=920,blank=True)
    email = models.EmailField(max_length=920)
    contact = models.CharField(max_length=12,blank=True)
    company_name = models.CharField(max_length=920,blank=True)
    product_interested_in = models.CharField(choices=product_type_choices,max_length=920,blank=True)
    status = models.CharField(choices=status_type_choices,max_length=920,blank=True)
    date_of_entry = models.DateTimeField(default=timezone.now, null=True)
    city = models.CharField(max_length=920,blank=True)
    profession = models.CharField(max_length=920,blank=True)

    def __str__(self):
            return str(self.pk)

    class Meta:
            verbose_name_plural = "All Leads Lists"
            verbose_name = "Lead"

class Team(models.Model):
    SUPER_ADMIN = 1
    ADMIN = 2
    TEAM = 3
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin'),
      (TEAM,'team')
    )
    sr_no = models.IntegerField()
    full_name = models.CharField(max_length=920)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    creation_date = models.DateTimeField(default=timezone.now, null=True)
    email = models.EmailField(max_length=920)
    contact = models.IntegerField()
    company_name = models.CharField(max_length=920)
    status = models.CharField(max_length=920)
    
    def __str__(self):
            return str(self.pk)

    class Meta:
            verbose_name_plural = "All Teams Lists"
            verbose_name = "Team"




