from django.shortcuts import render,redirect
from django.contrib import messages
from .models import appliedjobs, businessproposal, contact, interestedinvestor, query, userregister

# Create your views here.
def index(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        return render(request,"index.html",{'current_user':current_user,'user':user})
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        emailid=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        ph=request.POST['phone']
        adhar=request.POST['adharno']
        user=request.POST['usertype']
        emailexists=userregister.objects.filter(EmailID=emailid)
        phexists=userregister.objects.filter(Mobile=ph)
        if emailexists:
            messages.error(request,"Email ID Already Exists")
        elif phexists:
            messages.error(request,"Phone Number Already Registered")
        elif passw!=cpass:
            messages.error(request,"Password does not Match")
        else:
            userregister(Name=name,EmailID=emailid,Password=passw,Mobile=ph,AdharNo=adhar,UserType=user).save()
            return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        emailid=request.POST['email']
        passw=request.POST['password']
        user1=request.POST['usertype']
        user=userregister.objects.filter(EmailID=emailid,Password=passw,UserType=user1)
        if user:
            request.session['EmailID']=emailid
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"login.html")
def logout(request):
    del request.session['EmailID']
    return redirect('/')

def busi_propo(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        if request.method=='POST':
            name=request.POST['name']
            bname=request.POST['bname']
            regno=request.POST['regno']
            ctgry=request.POST['bcategory']
            objective=request.POST['propobjective']
            lifetime=request.POST['lifetime']
            xprnce=request.POST['experience']
            skillset=request.POST['skillset']
            cntctno=request.POST['contactno']
            address=request.POST['address']
            businessproposal(Name=name,BName=bname,CRegNo=regno,Category=ctgry,Objective=objective,Lifetime=lifetime,Experience=xprnce,SkillSet=skillset,ContactNo=cntctno,Address=address).save()
            return redirect('/')
        return render(request,"businessproposal.html",{'user':user})
def view_propo(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        data=businessproposal.objects.filter(Name=user.Name)
        return render(request,"viewproposal.html",{'data':data})
def allproposal(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        propo=businessproposal.objects.filter(Status='accepted') 
        return render(request,"allproposals.html",{'propo':propo,'user':user})
    
def update_bproposal(request,id):
    propo=businessproposal.objects.get(id=id)
    if request.method=='POST':
            bname=request.POST['bname']
            regno=request.POST['regno']
            ctgry=request.POST['bcategory']
            objective=request.POST['propobjective']
            lifetime=request.POST['lifetime']
            xprnce=request.POST['experience']
            skillset=request.POST['skillset']
            cntctno=request.POST['contactno']
            address=request.POST['address']
            propo.BName=bname
            propo.CRegNo=regno
            propo.Category=ctgry
            propo.Objective=objective
            propo.Lifetime=lifetime
            propo.Experience=xprnce
            propo.SkillSet=skillset
            propo.ContactNo=cntctno
            propo.Address=address
            propo.save()
            return redirect('/')
    return render(request,"updateproposal.html",{'propo':propo})
def my_profile(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        return render(request,"myprofile.html",{'user':user})
def update_profile(request,id):
    user=userregister.objects.get(id=id)
    if request.method=='POST':
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        ph=request.POST['phone']
        adhar=request.POST['adharno']
        user1=request.POST['usertype']
        user.Password=passw
        user.Mobile=ph
        user.AdharNo=adhar
        user.UserType=user1
        if passw==cpass:
            user.save()
        else:
            messages.error(request,"password doesnt match")
    return render(request,"updateprofile.html",{'user':user})
def query_func(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        if request.method=='POST':
            name=request.POST['name']
            myquery=request.POST['query']
            query(Name=name,Query=myquery).save()
            return redirect('/')
        return render(request,"addquery.html",{'user':user})
def viewquery(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        data=query.objects.filter(Name=user.Name)
        return render(request,"viewquery.html",{'data1':data})
    return render(request,"viewquery.html")
def applyjob(request,id):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        jobid=businessproposal.objects.get(id=id)
        if request.method=='POST':
            bman=request.POST['bname']
            bname=request.POST['bsname']
            applcnt=request.POST['applicant']
            nperiod=request.POST['notice']
            esalary=request.POST['salary']
            appliedjobs(BusinessMan=bman,Business=bname,Applicant=applcnt,NoticePeriod=nperiod,ExpectedSalary=esalary).save()
            return redirect('/')
        return render(request,"applyjobs.html",{'jobid':jobid,'user':user})
def viewjobs(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        data=appliedjobs.objects.filter(Applicant=user.Name)
        bdata=appliedjobs.objects.filter(BusinessMan=user.Name)
        if request.method=='POST':
            bdata1=appliedjobs.objects.get(BusinessMan=user.Name)
            status=request.POST['application']
            bdata1.Status=status
            bdata1.save()
            return redirect('/')
        return render(request,"viewjobs.html",{'data1':data,'bdata':bdata})
def investorinterest(request,id):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        jobid=businessproposal.objects.get(id=id)
        if request.method=='POST':
            bman=request.POST['bname']
            bname=request.POST['bsname']
            applcnt=request.POST['applicant']
            itype=request.POST['itype']
            amt=request.POST['iamount']
            itime=request.POST['itime']
            interestedinvestor(BusinessMan=bman,Business=bname,Applicant=applcnt,InvestmentType=itype,Amount=amt,TimeofInvestment=itime).save()
            return redirect('/')
        return render(request,'investorinterest.html',{'jobid':jobid,'user':user})
def viewinterest(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userregister.objects.get(EmailID=current_user)
        data=interestedinvestor.objects.filter(BusinessMan=user.Name) 
        bdata=interestedinvestor.objects.filter(Applicant=user.Name)
        if request.method=='POST':
            bdata1=interestedinvestor.objects.get(BusinessMan=user.Name)
            status=request.POST['application']
            bdata1.Status=status
            bdata1.save()
            return redirect('/')
        return render(request,"interests.html",{'data1':data,'bdata':bdata})
def contacts(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['message']
        contact.objects.create(Name=name,Email=email,Message=msg)
        print("hello")
        return redirect('/')