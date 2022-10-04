from decimal import Context
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from django.template import loader
from django.contrib import messages
from fyp.decorators import allowed_users
from fyp.forms import userregistrationform
from fyp.models import Car
from fyp.models import Card
from fyp.models import Residents
from fyp.models import Guests
from fyp.models import Admin
# generate random integer values
from random import seed
from random import randint
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import userregistrationform 
from django.contrib.auth.decorators import login_required
from .decorators import  allowed_users, admin_only
from django.contrib.auth.models import Group
from fyp.models import temproryresidentdata
from fyp.models import history
import datetime


#Function for Welcome PAge
def Welcome(request):
    return render(request,'welcomepage.html')
@login_required(login_url="Login")   
def index(request):
    return render(request,'index.html')

@login_required(login_url="Login")
@admin_only
def Register(request):
    if request.method=="POST":

        form=userregistrationform(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name="gateentryoperator")
            user.groups.add(group)

            messages.success(request,f'{{username}} is successfully registered')
            return redirect('Login')
    else:
        form=userregistrationform()

    context={
        "form":form
    }
    return render(request,'Register.html',context)

#Function to detete residents details
@login_required(login_url="Login")
def delete_resident(request,id):
    if request.method=='POST':
        pi=Residents.objects.get(pk=id) #get id of selected resdient entry  
        cad=Card.objects.get(Card_id=pi.Card_id)  #get the card details of that resident
        car=Car.objects.get(Car_Plate_number=pi.Car_Plate_number) #get car detail of that resident
        car.delete() 
        cad.delete()
        pi.delete()
    resident=Residents.objects.all()   #get all residents
    car=Car.objects.all()              #get all cars
    card=Card.objects.all()            #get all cards
    context={
        "Residents":resident,
        "car":car,
        "card":card,
    }
    return render(request,'ViewDetailsResident.html',context)


#Function to detete Guest details
@login_required(login_url="Login")
def delete_Guest(request,id):
    if request.method=='POST':
        pi=Guests.objects.get(pk=id)  #get id of selected Guest entry
        cad=Card.objects.get(Card_id=pi.Card_id) #get the card details of that Guest
        car=Car.objects.get(Car_Plate_number=pi.Car_Plate_number) #get car detail of that Guest
        car.delete()
        cad.delete()
        pi.delete()
    guest=Guests.objects.all() #get all residents
    car=Car.objects.all()      #get all cars
    card=Card.objects.all()    #get all cards
    context={
        "Guests":guest,
        "car":car,
        "card":card,
    }
    return render(request,'ViewDetailsGuest.html',context)  

#Function to show details of selected Resident in form to edit    
@login_required(login_url="Login")
def Edit_Resident(request,id):
    pi=Residents.objects.get(pk=id)
    car=Car.objects.get(Car_Plate_number=pi.Car_Plate_number)
    context={
        'data':pi,
        'car':car
    }
    return render(request,'EditResident.html',context)
#Function to update the Details of selected Resident
@login_required(login_url="Login")
def Residentupdate(request,id):
    try:
        F_name=request.POST.get('First_Name')
        L_name=request.POST.get('Last_Name')
        cnic=request.POST.get('CNIC')
        Car_name=request.POST.get('Car_Name')
        Car_Plate_Number=request.POST.get('Car_Plate_number')
        H_no=request.POST.get('H_no')
        Street=request.POST.get('Street')
        Sector=request.POST.get('Sector')
        Phone_number=request.POST.get('Phone_Number')
        re=Residents.objects.get(Resident_id=id)
        print(re.Car_Plate_number)
        # if re.Car_Plate_number != Car_Plate_Number:#check for car plate number updatation
        ca=Car.objects.get(Car_Plate_number=re.Car_Plate_number)
        print(ca.Car_Plate_number)
        ca.Name=Car_name
        ca.Car_Plate_number=Car_Plate_Number
        ca.save()
        card_var=Card.objects.get(Card_id=re.Card_id)
        card_var.Car_Plate_number=ca
        card_var.save()
        re.Car_Plate_number=ca
        re.First_Name=F_name
        re.Last_Name=L_name
        re.CNIC=cnic
        re.House_no=H_no
        re.Street=Street
        re.Sector=Sector
        re.Phone_Number=Phone_number
        re.save()
        resident=Residents.objects.all()
        car=Car.objects.all()
        card=Card.objects.all()
        context={
            "Residents":resident,
            "car":car,
            "card":card,
        }
    except:
        return render(request,'ViewDetailsResident.html',context)
    return render(request,'ViewDetailsResident.html',context)

#Function to show details of selected Guest in form to edit    
@login_required(login_url="Login")
def Edit_Guest(request,id):
    pi=Guests.objects.get(pk=id)
    car=Car.objects.get(Car_Plate_number=pi.Car_Plate_number)
    context={'data':pi,
    'car':car
    }
    return render(request,'EditGuest.html',context) 
#Function to update the Details of selected Guest
@login_required(login_url="Login")
def Guestupdate(request,id):
    try:
        F_name=request.POST.get('First_Name')
        L_name=request.POST.get('Last_Name')
        cnic=request.POST.get('CNIC')
        Car_name=request.POST.get('Car_Name')
        Car_Plate_Number=request.POST.get('Car_Plate_number')
        H_no=request.POST.get('H_no')
        Street=request.POST.get('Street')
        Sector=request.POST.get('Sector')
        re=Guests.objects.get(Guest_id=id)
        print(re.Car_Plate_number)
        ca=Car.objects.get(Car_Plate_number=re.Car_Plate_number)
        ca.Name=Car_name
        ca.Car_Plate_number=Car_Plate_Number
        ca.save()
        re.Car_Plate_number=ca
        re.First_Name=F_name
        re.Last_Name=L_name
        re.CNIC=cnic
        re.House_no=H_no
        re.Street=Street
        re.Sector=Sector
        re.save()
        guest=Guests.objects.all()
        car=Car.objects.all()
        card=Card.objects.all()
        context={
            "Guests":guest,
            "car":car,
            "card":card,
        }
    except:
        return render(request,'ViewDetailsGuest.html',context)

    return render(request,'ViewDetailsGuest.html',context)  


@login_required(login_url="Login")
#Function to verify Card(barcode) 


@login_required(login_url="Login")
def barcode(request):
    if request.method=='POST':
        nam=request.POST.get('bid')
        name=int(nam)
        name=name//10
        try:
            cad=Card.objects.get(Barcode_id=name)
           
        except:
            context={
            "error_message":"Card is not authenticated"
            }
            return render(request,'barcode.html',context)
        if cad.type=='guest':
            guest=Guests.objects.get(Card_id=cad.Card_id)
            History=history.objects.all()
            try:
                if guest.isentered==False:
                    
                    history.objects.create(Guest_id=guest.Guest_id,Entry_time=datetime.datetime.now())
                    guest.isentered=True
                    guest.save()
                else:
                    for hist in History:
                        if hist.Guest_id==guest.Guest_id:
                            if hist.Exit_time==None:
                                hist.Exit_time=datetime.datetime.now()
                                hist.Guest_id=guest.Guest_id
                                hist.save()
                    guest.isentered=False
                    guest.save()
            except:
                return render(request,'barcode.html',context)
        context={
                        "msg":cad.Car_Plate_number,
                        "message":"Card is Registered Against Car Plate Number"
                        
                    }
        
        return render(request,'barcode.html',context)
    return render(request,'barcode.html')
    
@login_required(login_url="Login")
def historys(request,id):
    guest=Guests.objects.get(Guest_id=id)
    History =history.objects.all()
    context={
        'guest':guest,
        'History':History,
    }
    return render(request,'historys.html',context)



#Function to get details of resident from form and save into Resident table 
@login_required(login_url="Login")
def ResidentRegistration(request):
    try:
        if 'submitforapproval' in request.POST:
            F_name=request.POST.get('First_Name')
            L_name=request.POST.get('Last_Name')
            cnic=request.POST.get('CNIC')
            Car_name=request.POST.get('Car_Name')
            Car_Plate_Number=request.POST.get('Car_Plate_number')
            H_no=request.POST.get('H_no')
            street=request.POST.get('Street')
            sector=request.POST.get('Sector')
            Phone_number=request.POST.get('Phone_Number')
            temproryresidentdata.objects.create(First_Name=F_name,Last_Name=L_name,CNIC=cnic,
                    Phone_Number=Phone_number,Car_Name=Car_name,Car_Plate_number=Car_Plate_Number,
                    House_no=H_no,Street=street,Sector=sector)
        elif request.method=='POST':
            
            F_name=request.POST.get('First_Name')
            L_name=request.POST.get('Last_Name')
            cnic=request.POST.get('CNIC')
            Car_name=request.POST.get('Car_Name')
            Car_Plate_Number=request.POST.get('Car_Plate_number')
            H_no=request.POST.get('H_no')
            street=request.POST.get('Street')
            sector=request.POST.get('Sector')
            Phone_number=request.POST.get('Phone_Number')
            bcode=randint(100000000000,999999999999)
            Car.objects.create(Car_Plate_number=Car_Plate_Number,Name=Car_name) #save car details of resident in car table
            car=Car.objects.get(Car_Plate_number=Car_Plate_Number)
            Card.objects.create(Car_Plate_number=car,Barcode_id=bcode,type="resident") #save Card details of resident in card table
            card=Card.objects.get(Car_Plate_number=Car_Plate_Number)
            
            Residents.objects.create(
                First_Name=F_name,Last_Name=L_name,CNIC=cnic,
                Phone_Number=Phone_number,Card_id=card,Car_Plate_number=car,
                House_no=H_no,Street=street,Sector=sector,type="resident") #save details Resident in table

            if 'Issuecard' in request.POST:
                re=Residents.objects.get(CNIC=cnic)
                context={
                        'type':'Resident',
                            're':re,
                            'car_name':car.Name,
                            'card':card
                    }
                return render(request,'IssueCard.html',context)
    except:
            return render(request,'ResidentRegistration.html')
    return render(request,'ResidentRegistration.html')

@login_required(login_url='Login')
def issuecard(request,id,type):
    if type=='resident':
        re=Residents.objects.get(Resident_id=id)
        car=Car.objects.get(Car_Plate_number=re.Car_Plate_number)
        card=Card.objects.get(Card_id=re.Card_id)
    elif type=='guest':
        re=Guests.objects.get(Guest_id=id)
        car=Car.objects.get(Car_Plate_number=re.Car_Plate_number)
        card=Card.objects.get(Card_id=re.Card_id)

    context={
                        'type':re.type,
                            're':re,
                            'car_name':car.Name,
                            'card':card
                    }
    return render(request,'IssueCard.html',context)


#Function to view details of residents 
@login_required(login_url="Login")
def ViewDetailsResident(request):
    resident=Residents.objects.all()
    car=Car.objects.all()
    card=Card.objects.all()
    context={
        "Residents":resident,
        "car":car,
        "card":card,
    }
    return render(request,'ViewDetailsResident.html',context)
#Function to view details of Guests
@login_required(login_url="Login")
def ViewDetailsGuest(request):
    guests=Guests.objects.all()
    car=Car.objects.all()
    card=Card.objects.all()
    context={
        "Guests":guests,
        "car":car,
        "card":card,
    }
    return render(request,'ViewDetailsGuest.html',context)


#Function to get details of Guest from form and save into Guest table 

@login_required(login_url="Login")
def GuestRegistration(request):
    try:
        if request.method=='POST':
            F_name=request.POST.get('First_Name')
            L_name=request.POST.get('Last_Name')
            cnic=request.POST.get('CNIC')
            Car_name=request.POST.get('Car_Name')
            Car_Plate_Number=request.POST.get('Car_Plate_number')
            H_no=request.POST.get('H_no')
            street=request.POST.get('Street')
            sector=request.POST.get('Sector')
            bcode=randint(100000000000,999999999999)
            Car.objects.create(Car_Plate_number=Car_Plate_Number,Name=Car_name) #save car details of Guest in car table
            car=Car.objects.get(Car_Plate_number=Car_Plate_Number)
            Card.objects.create(Car_Plate_number=car,Barcode_id=bcode,type="guest")#save Card details of Guest in card table
            
            card=Card.objects.get(Car_Plate_number=Car_Plate_Number)
            Guests.objects.create(
                First_Name=F_name,Last_Name=L_name,CNIC=cnic,
                Card_id=card,Car_Plate_number=car,
                House_no=H_no,Street=street,Sector=sector,type="guest")#save details Guest in table

            if 'Issuecard' in request.POST:
                re=Guests.objects.get(CNIC=cnic)
                context={
                    'type':'Guest',
                        're':re,
                        'car_name':car.Name,
                        'card':card
                }
                return render(request,'IssueCard.html',context)
    except:
            return render(request,'GuestRegistration.html')

    return render(request,'GuestRegistration.html')



def Login(request):
    
    return render(request,'login.html')

@login_required(login_url="Login")
def profile(request):
    
    return render(request,'profile.html')

# @allowed_users(allowed_roles=['gateentryoperator'])   
@login_required(login_url="Login") 
@admin_only

def approvalpage(request):
    tempresident=temproryresidentdata.objects.all()
   
    context={
        'data':tempresident,
        
    }
    return render(request,'approvalpage.html',context)
@login_required(login_url="Login")
def delete_tempresident(request,id):
   
    pi=temproryresidentdata.objects.get(pk=id) #get id of selected resdient entry  
    pi.delete()
    return redirect('approvalpage')
@login_required(login_url="Login")
def approve_tempresident(request,id):
    pi=temproryresidentdata.objects.get(pk=id)
   
    Car.objects.create(Car_Plate_number=pi.Car_Plate_number,Name=pi.Car_Name) #save car details of resident in car table
    car=Car.objects.get(Car_Plate_number=pi.Car_Plate_number)
    Card.objects.create(Car_Plate_number=car,Barcode_id=randint(100000000000,999999999999)) #save Card details of resident in card table
    card=Card.objects.get(Car_Plate_number=pi.Car_Plate_number)
        
    Residents.objects.create(
            First_Name=pi.First_Name,Last_Name=pi.Last_Name,CNIC=pi.CNIC,
            Phone_Number=pi.Phone_Number,Card_id=card,Car_Plate_number=car,
            House_no=pi.House_no,Street=pi.Street,Sector=pi.Sector) #save details Resident in table
    pi.delete()
    return redirect('approvalpage')


