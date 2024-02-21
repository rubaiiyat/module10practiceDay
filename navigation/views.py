from django.shortcuts import render
import datetime
def home(request):
    data={'name':"abir rubaiyat",'varsity':"PUB",'id':43,'dept':"CSE",'emptyString':"",'randomNum':"654673",'datetime':datetime.datetime.now(),'blog_time':(2024,3,6),'lineNum':"Inspect Template Context: If you're using Django Debug Toolbar or any other debugging tools",'python':["python","is","the","best"],'stdInfo':[
        {'name':"josh",'age':"10"},
        {'name':"David",'age':"15"},
        {'name':"Caroline",'age':"25"}
    ]}

 
    return render(request,'home.html',data)

   

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
