from django.shortcuts import render
from .models import member
# Create your views here.
def add_member(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        num=request.POST.get('card')
        year=request.POST.get('year')
        birth=request.POST.get('birth')
        member.objects.create(
            name=name,
            famname=fname,
            cardnum=num,
            year=year,
            birth=birth
        )
    return render(request,'member.html')

def affich(request):
    impo=member.objects.all()
    return render(request,'affich.html',{'data':impo})