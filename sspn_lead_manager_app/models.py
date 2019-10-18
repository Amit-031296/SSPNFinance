from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from model_utils.managers import InheritanceManager

# Create your models here.

class AllLeads(models.Model):
        city_choices=(('Mumbai','Mumbai'),
        ('Delhi','Delhi'),
        ('Banglore','Banglore'),
        ('Pune','Pune'),
        ('Ahmedabad','Ahmedabad'),
        ('Other','Other'))
        profession_type_choices=(('Salaried','Salaried'),
                        ('Business','Business'),
                        ('Self Employed','Self Employed'),
                        ('Other','Other'))
        product_type_choices=(('MicroFinance','MicroFinance'),
                        ('InstantSalary','InstantSalary'),
                        ('ConsumerFinance','ConsumerFinance'))
        status_type_choices=(('Pending','Pending'),
                        ('InProcess','InProcess'),
                        ('Approved','Approved'),
                        ('Rejected','Rejected'))
        sr_no = models.IntegerField(default=1)
        full_name = models.CharField(max_length=920)
        gender = models.CharField(max_length=920,blank=True)
        email = models.EmailField(max_length=920)
        contact = models.CharField(max_length=12,blank=True)
        company_name = models.CharField(max_length=920,blank=True)
        product_interested_in = models.CharField(choices=product_type_choices,max_length=920,blank=True)
        status = models.CharField(choices=status_type_choices,max_length=920,blank=True,default='Pending')
        date_of_entry = models.DateTimeField(default=timezone.now, null=True)
        city = models.CharField(choices=city_choices,max_length=920,blank=True)
        profession = models.CharField(choices=profession_type_choices,max_length=920,blank=True)
        
        def __str__(self):
            return str(self.pk)
        
        class Meta:
            verbose_name_plural = "All Leads Lists"
            verbose_name = "Lead"

class Team(AbstractUser):
    SUPER_ADMIN = 1
    ADMIN = 2
    TEAM = 3
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin'),
      (TEAM,'team')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=3)
    contact = models.CharField(blank=True,max_length=920)

    
    def __str__(self):
            return str(self.pk)

    class Meta:
            verbose_name_plural = "All Teams Lists"
            verbose_name = "Team"




