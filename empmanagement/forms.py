from django import forms


class EmployeeForm(forms.Form):
    Emp_code=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    position=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    contact=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
    city=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    salary=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))