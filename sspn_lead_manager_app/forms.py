from django import forms
from sspn_lead_manager_app.models import AllLeads,Team
from bootstrap_modal_forms.forms import BSModalForm

class AllLeadsForm(BSModalForm):
    class Meta:
        model= AllLeads
        fields=('product_interested_in',
        'status',
        'full_name',
        'gender',
        'email',
        'contact',
        'company_name',
        'city',
        'profession') 

class TeamForm(BSModalForm):
    class Meta:
        model = Team
        fields=('full_name',
        'email',
        'role',
        'contact',
        'status')