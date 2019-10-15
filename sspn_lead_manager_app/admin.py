from django.contrib import admin
from sspn_lead_manager_app.models import AllLeads,Team

# Register your models here.

class AllLeadsAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "sr_no",
        "full_name",
        "gender",
        "contact",
        "company_name",
        "product_interested_in",
        "date_of_entry"
    ]

class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "sr_no",
        "full_name",
        "role",
        "company_name"
    ]

admin.site.register(AllLeads,AllLeadsAdmin)
admin.site.register(Team,TeamAdmin)

