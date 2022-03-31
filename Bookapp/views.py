from django.shortcuts import render, redirect
from .models import Books
from django.http import HttpResponse


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        data = Books.objects.filter(aval_quantity__gte=1)
        return render(request, 'store.html', {'data': data})
    else:
        return HttpResponse("<center>Invailed user login first<br><a href="'/login/'">Login</a>")

def outOfStoks(request):
    if request.user.is_authenticated:
        data = Books.objects.filter(aval_quantity__lte=0)
        return render(request, 'outstoks.html', {'data': data})
    else:
        return HttpResponse("<center>Invailed user login first<br><a href="'/login/'">Login</a>")

def addBook(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            bname=request.POST.get('bname')
            btitle=request.POST.get('title')
            author=request.POST.get('author')
            total=request.POST.get('total')
            Books.objects.create(bname=bname,b_title=btitle,b_author=author,
                                 total_quantity=total,aval_quantity=total)
            return redirect('/library/')
        return render(request,'create.html')

    else:
        return HttpResponse("<center>Invailed user login first<br><a href="'/login/'">Login</a>")



def editBook(request,bid):
    if request.user.is_authenticated:
        data=Books.objects.get(id=bid)
        if request.method=="POST":
            bname=request.POST.get('bname')
            btitle=request.POST.get('title')
            author=request.POST.get('author')
            total=request.POST.get('total')
            aval=request.POST.get("aval")
            print(bname,btitle,author,total,aval)
            data.bname=bname
            data.b_title=btitle
            data.b_author=author
            data.total_quantity=total
            data.aval_quantity=aval
            data.save()
            print('data saved successfully!')
            return redirect('/library/')


        return render(request,'edit.html',{'data':data})
    else:
        return HttpResponse("<center>Invailed user login first<br><a href="'/login/'">Login</a>")
def listOut(request,bid):
    data=Books.objects.get(id=bid)
    data.aval_quantity=data.aval_quantity-1
    data.save()
    return redirect('/library/')
def deleteBook(request,bid):
    if request.user.is_authenticated:
        data=Books.objects.filter(id=bid)
        print(data)
        data.delete()
        print('book deleted')
        return redirect('/library/')
    else:
        return HttpResponse("<center>Invailed user login first<br><a href="'/login/'">Login</a>")


