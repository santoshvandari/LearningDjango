# from django.http import HttpResponse,HttpResponseRedirect
# from django.shortcuts import render,redirect
# # from .form import UserDataForm
# def home(request):
#     return render(request,"index.html")

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

# # def DynamicUrl(request):
# #     return HttpResponse("<h1> Dynamic URL Page</h1>")

# # def DynamicContent(request,data):
# #     Data=data
# #     return HttpResponse(f"The Url is: <b>http://127.0.0.1:8000/Dynamic/{Data}</b>")



# def ifelse(request):
#     data={"numbers":[6,20,12,36,355,694,52,10,25,63,212,5,1,54,845,201351]}
#     return render(request,"ifelse.html",data)

# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")

# def services(request):
#     return render(request,"services.html")

# # def form(request):
# #     data=None
# #     try:
# #         # data={
# #         #     'name':request.GET['name'],
# #         #     'address':request.GET.get('address'),
# #         #     'msg':request.GET.get('msg')
# #         # }
# #         if request.method=='POST':
# #             data={
# #                 'name':request.POST['name'],
# #                 'address':request.POST.get('address'),
# #                 'msg':request.POST.get('msg')
# #             }
# #             # return HttpResponseRedirect("/")
# #             return redirect("/")
# #     except:
# #         pass
# #     return render(request,'form.html',data)


# def form(request):
#     data=UserDataForm()
#     return render(request,"form.html",{'form':data})





# def submit(request):
#     try:
#         if request.method=='POST':
#             data={
#                 'name': request.POST.get("name"),
#                 'add': request.POST.get("address"),
#                 'msg': request.POST.get("msg"),
#                 'email': request.POST.get("email"),
#             }
#     except:
#         pass
#     return render(request,"submit.html",data)
