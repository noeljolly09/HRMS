from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import employeeDetails,complain,Leave

# Create your views here.

def home(request):

    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['userpass']

        user = auth.authenticate(username=uname,password=upass)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')


        else:
            messages.error(request, 'user login unsuccesfull')
            
            return redirect('/')

    else:

        return render(request, 'index.html')

def dashboard(request):
    return render(request, 'main.html')

def signup(request):


    if request.method == 'POST':
        user_name = request.POST['username']
        fname = request.POST['uname']
        user_email = request.POST['email']
        user_p1 = request.POST['p1']
        user_p2 = request.POST['p2']

        if user_p1==user_p2:

            if User.objects.filter(username=user_name).exists():
                print('username already taken')
            elif User.objects.filter(email=user_email).exists():
                print('email already exist')
            else:
                user = User.objects.create_user(username=user_name,email=user_email,first_name=fname,password=user_p1)
                user.save()
                print('user created')
                return redirect('/')

        else:
            print('Password are not same')
        return redirect('/')


    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def addEmployee(request):

    if request.method == 'POST':
        a = request.POST['first_name']
        b = request.POST['last_name']
        c = request.POST['address']
        d = request.POST['email']
        e = request.POST['dob']
        f = request.POST['phone']
        g = request.POST['bsalary']
        # h = request.POST['leaves']

        employeeDetails(firstName=a,lastName=b,address=c,email=d,DOB=e,phoneNumber=f,salary=g).save()
        return redirect('/dashboard')
    
    else:
        return render(request , 'addemp.html')

def removeEmployee(request):

    details = employeeDetails.objects.all()

    if request.method == 'POST':
        a = request.POST['empid']
        emp = employeeDetails.objects.get(id=a)
        emp.delete()

        return render(request, 'remove_emp.html', {'details':details})
    else:
        return render(request, 'remove_emp.html', {'details':details})

def allEmployee(request):

    details = employeeDetails.objects.all()
    
    return render(request, 'all_emp.html', {'details':details})

def addComplain(request):
    
    if request.method == 'POST':
        a = request.POST['date']
        b = request.POST['complain']
        c = request.POST['description']

        complain(date=a,Type=b,complain_text=c).save()
        return redirect('/dashboard')
    
    else:
        return render(request, 'add_complain.html')

def allComplain(request):

    details = complain.objects.all()
    
    return render(request, 'all_complain.html', {'details':details})

def applyLeave(request):
    things = employeeDetails.objects.all()

    if request.method == 'POST':
        e = request.POST['emp_name']
        a = request.POST['name']
        b = request.POST['from']
        c = request.POST['to']
        d = request.POST['reason']
    

        Leave(apply_date=a,from_date=b,to_date=c,Reason=d,status='UNAPPROVED',employee=employeeDetails.objects.get(id=e)).save()
        return redirect('/dashboard')
    else:
        return render(request, 'apply_leave.html',{'things':things})

def approvalLeave(request):

    things = employeeDetails.objects.all()

    details = Leave.objects.all()

    return render(request, 'approval_leave.html',{'details':details})

def allLeave(request):
    details = Leave.objects.all()

    return render(request, 'all_leave.html', {'details':details})

def allSalary(request):
    details = employeeDetails.objects.all()

    return render(request, 'all_salary.html',{'details':details})

def Accept(request, id):
    print(id)
    print( Leave.objects.get(id=id))
    Leave.objects.filter(id=id).update(status='APPROVED')
    return redirect('/leaveapproval')

def Reject(request, id):
    print(id)
    print( Leave.objects.get(id=id))
    Leave.objects.filter(id=id).update(status='DECLINED')
    return redirect('/leaveapproval')