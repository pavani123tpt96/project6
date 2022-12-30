from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'pavanidivya'}
    return render(request,'jinja_print.html',context=d)
def detail_view(request):
    d={'college':'vijayawada narayana'}
    return render(request,'jinja_print.html',d)


    