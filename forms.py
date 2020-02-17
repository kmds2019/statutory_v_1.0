from django import forms
from tbl.models import statutory_details

class StatutoryDetailsInputForm(forms.ModelForm):
    class Meta:
        model = statutory_details
        fields = ['country','domain',\
        'act_name','rule_name','is_active','is_custom','created_by',\
        'created_on']
        """
        fields = ['statutory_id','country','domain',\
        'act_name','rule_name','is_active','is_custom','created_by',\
        'created_on','updated_by','updated_on']
        """
        act_name = forms.CharField(max_length=200)
        rule_name = forms.CharField(max_length=200)
        country_id = forms.IntegerField()
        domain_id = forms.IntegerField()
        def save(self):
            new_statutory = statutory_details.objects.create(
            country=self.cleaned_data['country'],
            domain=self.cleaned_data['domain'],
            act_name=self.cleaned_data['act_name'],
            rule_name=self.cleaned_data['rule_name'])
            return new_statutory
        def clean_name(self):
            return self.cleaned_data['act_name'].lower()
