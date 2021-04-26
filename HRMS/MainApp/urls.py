from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.home),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('addemployee',views.addEmployee, name='addEmployee'),
    path('removeemployee',views.removeEmployee, name='removeEmployee'),
    path('allemployee',views.allEmployee, name='allEmployee'),
    path('addcomplain',views.addComplain,name='addcomplain'),
    path('allcomplain',views.allComplain,name='allcomplain'),
    path('applyleave',views.applyLeave,name='applyleave'),
    path('leaveapproval',views.approvalLeave,name='leaveapproval'),
    path('allleave',views.allLeave,name='allleave'),
    path('allsalary',views.allSalary,name='allsalary'),
    path('accept/<int:id>',views.Accept),
    path('reject/<int:id>',views.Reject)


]