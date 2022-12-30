from django.shortcuts import render

# Create your views here.
def user(request):
    d={'mobile':[9966647524]}
    return render(request,'user.html',context=d)
def user1(request):
    d={'data':'pendrive'}
    return render(request,'user.html',d)
