from django.shortcuts import render,redirect,get_object_or_404
from .models import member
from .Forms import member_form 


def remove_member(request,member_id):
    obj = get_object_or_404(member, id=member_id)
    obj.delete()
    return redirect(affich)
    
def edit_member(request,member_id):
    obj = get_object_or_404(member, id=member_id)
    if request.method == 'POST':
        form = member_form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(affich)
    else:
        form = member_form(instance=obj)
    return render(request, 'member.html', {'form': form,'is_edit':True,'idm':member_id})
# Create your views here.
def add_member(request):
    if request.method == 'POST':
        form=member_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(affich) 
    form=member_form()
    return render(request,'member.html',{'form':form,'is_edit':False})

def affich(request):
    impo=member.objects.all()
    return render(request,'affich.html',{'data':impo})

