from django.shortcuts import render,redirect
from .models import Member
# Create your views here.


def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html',{'mem':mem})


# def add(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         department = request.POST.get('department')
#         email = request.POST.get('email')
#         profile_img=request.POST.get('picture')
#         mem = Member(firstname=firstname, lastname=lastname, department=department, email=email ,profile_img= profile_img)
#         mem.save()
#         return redirect('/')
def add(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        department = request.POST.get('department')
        email = request.POST.get('email')
        profile_img = request.FILES.get('picture')
        mem = Member(firstname=firstname, lastname=lastname, department=department, email=email,profile_img=profile_img)
        mem.save()
        return redirect('/')
    return render(request,'add.html')




def delete(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('/')


def update(request,id):
    mem = Member.objects.get(id=id)
    if request.method == 'POST':
        mem.firstname = request.POST.get('firstname')
        mem.lastname = request.POST.get('lastname')
        mem.department = request.POST.get('department')
        mem.email = request.POST.get('email')
        mem.profile_img = request.FILES.get('picture')
        mem.save()
        return redirect('/')
    
    return render(request,'add.html',{'mem':mem})