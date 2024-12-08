from django.shortcuts import render,redirect
from django.views import View
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



# Create your views here.



class HomeView(View):
    def get(self,request):
        data=Employee.objects.all()
        return render(request,"home.html",{"data":data} )



class AddEmployee(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,"add.html",{"form":form})
    
    def post(self,request):
        formdata=EmployeeForm(data=request.POST)
        if formdata.is_valid():
            Emp_code=formdata.cleaned_data.get('Emp_code')
            name=formdata.cleaned_data.get('name')
            position=formdata.cleaned_data.get('position')
            contact=formdata.cleaned_data.get('contact')
            city=formdata.cleaned_data.get('city')
            salary=formdata.cleaned_data.get('salary')
            
            Employee.objects.create(Emp_code=Emp_code,name=name,position=position,contact=contact,city=city,salary=salary)
            return redirect("home")
        return render(request,"add.html",{"form":formdata})

class editemployeeview(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        emp=Employee.objects.get(id=tid)
        form=EmployeeForm(initial={"Emp_code":emp.Emp_code,"name":emp.name,"position":emp.position,"contact":emp.contact,"city":emp.city,"slary":emp.salary})
        return render(request,"edit.html",{"form":form})
    
    def post(self,request,**kwargs):
        formdata=EmployeeForm(data=request.POST)
        tid=kwargs.get('id')
        task=Employee.objects.get(id=tid)
        if formdata.is_valid():
            Emp_code=formdata.cleaned_data.get('Emp_code')
            name=formdata.cleaned_data.get('name')
            position=formdata.cleaned_data.get('position')
            contact=formdata.cleaned_data.get('contact')
            city=formdata.cleaned_data.get("city")
            salary=formdata.cleaned_data.get('salary')
            task.Emp_code=Emp_code
            task.name=name
            task.position=position
            task.contact=contact
            task.city=city
            task.salary=salary
            task.save()

            return redirect('home')
        return render(request,"edit.html",{"form":formdata})
    
class deleteemployee(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        task=Employee.objects.get(id=tid)
        task.delete()
        return redirect('home')  
    
    
    
    
def SearchEmployee(request):
    if request.method == 'GET':
        query=request.GET.get('query')
        if query:
            data=Employee.objects.filter(position__icontains=query)
            return render(request,'searchbar.html',{'data':data})
        else:
            print('No information to show')
            return request(request,'searchbar.html',{})
    
    
    
    
    
    
def changepassword(request):

    if request.method=='POST':
        
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,"record updated")
            return redirect('home')
    else:
        fm=PasswordChangeForm(user=request.user)
        
    return render(request,'changepswd.html',{"fm":fm})
    
