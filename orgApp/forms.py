from django import forms
from orgApp import models


class CategoryMainRegForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = '__all__'


class OrganisationMainRegForm(forms.ModelForm):

    class Meta:
        model = models.Organisation
        fields = '__all__'


class OrgDetailMAinRegForm(forms.ModelForm):

    class Meta:
        model = models.orgDetail
        fields = '__all__'


class OrgProjectMainRegForm(forms.ModelForm):

    class Meta:
        model = models.orgProject
        fields = '__all__'


"""
If we need any extra features in form we will create a class which will extends those class accordingly...
"""
