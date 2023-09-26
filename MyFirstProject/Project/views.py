from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .form import UserDataForm
from .models import ContactData,FormData,FileUpload,UserData
def home(request):
    # return HttpResponse("Hello World")
    return render(request,"index.html")

# def loop(request):
#     # return HttpResponse(url)
#     data={
#         'language':["Java","C++","Python","JavaScript"],
#         "info":[
#             {"name":"Santosh Bhandari","Address":"Birtamode"},
#             {"name":"Manoj Oli","Address":"Surunga"}
#         ]
#     }
#     return render(request,"loop.html",data)

# def DynamicUrl(request):
#     return HttpResponse("<h1> Dynamic URL Page</h1>")

# def DynamicContent(request,data):
#     Data=data
#     return HttpResponse(f"The Url is: <b>http://127.0.0.1:8000/Dynamic/{Data}</b>")



# def ifelse(request):
#     data={"numbers":[6,20,12,36,355,694,52,10,25,63,212,5,1,54,845,201351]}
#     return render(request,"ifelse.html",data)

def about(request):
    return render(request,"about.html")

def contact(request):
    datas=ContactData.objects.all()
    datas=ContactData.objects.all().order_by("-id")
    datas=ContactData.objects.all()[0:2]
    return render(request,"contact.html",{'data':datas})

def services(request):
    return render(request,"services.html")

# def form(request):
#     data=None
#     try:
#         # data={
#         #     'name':request.GET['name'],
#         #     'address':request.GET.get('address'),
#         #     'msg':request.GET.get('msg')
#         # }
#         if request.method=='POST':
#             data={
#                 'name':request.POST['name'],
#                 'address':request.POST.get('address'),
#                 'msg':request.POST.get('msg')
#             }
#             # return HttpResponseRedirect("/")
#             return redirect("/")
#     except:
#         pass
#     return render(request,'form.html',data)


def form(request):
    data=UserDataForm()
    return render(request,"form.html",{'form':data})





def submit(request):
    try:
        if request.method=='POST':
            data={
                'name': request.POST.get("name"),
                'add': request.POST.get("address"),
                'msg': request.POST.get("msg"),
                'email': request.POST.get("email"),
            }
    except:
        pass
    return render(request,"submit.html",data)


def formdata(request):
    msg=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('msg')
        try: 
            insert=FormData(name=name,email=email,message=message)
            insert.save()
            msg="Message Sent Successfully!!"
        except Exception as e:
            msg="Failed to Sent Message!! Please Try Again!!"
    return render(request,"formdata.html",{"msg":msg})

def file(request):
    msg=""
    if request.method=='POST':
        name=request.POST.get('name')
        file=request.FILES['file']
        # filename=request.FILES['file']['name']
        # filename=str(file)
        # if filename.endswith(".png"):
        #     print("Yes it is")
        # else:
        #     print("not it's noe")
        try:
            upload=FileUpload(name=name,file=file)
            # if upload.is_valid():
            upload.save()
            # handle_uploaded_file(request.FILES["file"])

            msg="File Successfully Uploaded!!!"
        except:
            msg="Failed to Upload File!!!"
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     handle_uploaded_file(request.FILES["file"])
        #     return HttpResponseRedirect("/success/url/")
    return render(request,"file.html",{'msg':msg})




def loginUser(request):
    request.session['msg']=""
    
    if request.method=='POST':
        user=request.POST.get("username")
        pwd=request.POST.get("password")
        try: 
            data=UserData.objects.filter(username=user,password=pwd)
            if data:
                request.session['user'] = data[0].username
                return redirect("/dashboard")
                
            else: 
                print("user Data Doesn't exit")
                request.session['msg']="Sorry!! Please Recheck Your Credential"
                return redirect("/login")
        except:
            request.session['msg']="Sorry!! Some Issue Arise!!!"
            return redirect("/login")
    if 'user' in request.session:
        return redirect(request,"dashboard.html")
    return render(request, "login.html",{'msg':request.session['msg']})




def logoutUser(request):
    del request.session['user']
    return redirect("/login")



def dashboard(request):
    userdata=""
    if 'user' in request.session:
        userdata=request.session["user"]
        return render(request,"dashboard.html",{'userdata':userdata})
    else:
        request.session['msg']="Sorry!! Please Login First!!!"
        return redirect("/login")




def custom404(request,exception):
    return render(request,"404.html",status=404)