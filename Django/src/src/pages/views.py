from django.http import HttpResponse
from django.shortcuts import render
def homepage_view(request,*args, **kwargs):
    print(request.user)
    return render(request,"home.html",{})
def contact_view(request,*args, **kwargs):
    print(request.user)
    return render(request,"contact.html",{})
def social_view(request,*args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Social Page</h1>")
def about_view(request,*args, **kwargs):
    my_context={
        "my_text": "This is about us",
        "my_number" : 113,
        "my_list": [4324,4324,5432]
    }
    print(request.user)
    return render(request,"about.html",my_context)