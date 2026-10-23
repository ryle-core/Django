from django.shortcuts import render
from app.models import Register
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')


def register_view(request):
    if request.method == "POST":
        student = Register(
          fullname =request.POST['fullname'] ,
          dob =request.POST['dob'],
          gender =request.POST['gender'],
          email =request.POST['email'],
           phone =request.POST['phone'],
           course =request.POST['course'],
           year =request.POST['year'],
           confirm_information=(
                request.POST.get('confirm_information') == 'on'
        ),
        )
        student.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def show(request):
    all = Register.objects.all()
    return render(request, 'show.html',{'all': all})
    
    
        
