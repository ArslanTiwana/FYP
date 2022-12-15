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
from fyp.models import history
import datetime
from PIL import Image
import cv2 
import requests
from pprint import pprint




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
        cardss=[]
        cars=[]
        pi=Residents.objects.get(pk=id) #get id of selected resdient entry
        cards=Card.objects.all()
        for card in cards:
            if card.Resident is not None:
                if(card.Resident.CNIC==pi.CNIC):
                    cardss.append(card)
        print(cardss)
        for card in cardss:
            car=Car.objects.get(Car_Plate_number=card.Car_Plate_number.Car_Plate_number)
            cars.append(car)
        print(cars)
        for card in cardss:
            card.delete()
        for car in cars:
            car.delete()
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
    re=Residents.objects.get(Resident_id=id)
    card=Card.objects.all()
    context={
        'data':re,
        'card':card
    }
    return render(request,'EditResident.html',context)
#Function to update the Details of selected Resident
@login_required(login_url="Login")
def Residentupdate(request,id):
    CarNames=[]
    CarNumbers=[]  
    cars=[]
    cards=[]
    F_name=request.POST.get('First_Name')
    L_name=request.POST.get('Last_Name')
    cnic=request.POST.get('CNIC')
    for x in range(0,100):
        Tag1='Car_Name'+str(x)
        Cn=request.POST.get(Tag1)
        if Cn is not None:
            CarNames.append(Cn)
        Tag2='Car_Plate_number'+str(x)
        cpno=request.POST.get(Tag2)
        if cpno is not None:
            CarNumbers.append(cpno.upper())
    H_no=request.POST.get('H_no')
    street=request.POST.get('Street')
    sector=request.POST.get('Sector')
    Phone_number=request.POST.get('Phone_Number')
    re=Residents.objects.get(Resident_id=id)
    re.First_Name=F_name
    re.Last_Name=L_name
    re.CNIC=cnic
    re.House_no=H_no
    re.Street=street
    re.Sector=sector
    re.Phone_Number=Phone_number
    re.save()
    re=Residents.objects.get(Resident_id=id)
    crd=Card.objects.all()
    for c in crd:
        if c.Resident is not None:
            if(c.Resident.CNIC==re.CNIC):
                cards.append(c)
    carr=Car.objects.all()
    for onecard in cards:
        for onecar in carr:
            if(onecar.Car_Plate_number==onecard.Car_Plate_number.Car_Plate_number):
                cars.append(onecar)
    newcars=0
    for index in range(len(CarNames)):
        newcars=newcars+1
        if newcars<=len(cars):
            cars[index].Car_Plate_number=CarNumbers[index]
            cars[index].Name=CarNames[index]
            cars[index].save()

            cards[index].Car_Plate_number=cars[index]
            cards[index].Resident=re
            cards[index].save()
        else:
            bcode=randint(100000000000,999999999999)
            Car.objects.create(Car_Plate_number=CarNumbers[index],Name=CarNames[index]) #save car details of resident in car table
            cars.append(Car.objects.get(Car_Plate_number=CarNumbers[index]))
            Card.objects.create(Car_Plate_number=cars[index],Barcode_id=bcode,type="resident",Resident=re) #save Card details of resident in card table
            cards.append(Card.objects.get(Car_Plate_number=cars[index]))
         
    resident=Residents.objects.all()
    car=Car.objects.all()
    card=Card.objects.all()
    context={
        "Residents":resident,
        "car":car,
        "card":card,
    }

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
        cdn=request.POST.get('Car_Plate_number')
        Car_Plate_Number=cdn.upper()
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
    
def alertOnHistory(cad):
    History=history.objects.all()
    historiesexittimes=[]
    for histo in History:
        if histo.Card_id==cad:
            if histo.Exit_time is not None:
                historiesexittimes.append(histo.Exit_time.hour*10000+histo.Exit_time.minute*100+histo.Exit_time.second)
    print(max(historiesexittimes))
    print(min(historiesexittimes))
    minlimittime=min(historiesexittimes)-(1*10000)
    maxlimittime=max(historiesexittimes)+(1*10000)
    current_date = datetime.datetime.now()
    timenow=current_date.hour*10000 +current_date.minute*100 +current_date.second

    if timenow<minlimittime:
        print("alert")
    elif timenow>maxlimittime:
        print("alert")

    avg=sum(historiesexittimes)/len(historiesexittimes)
    print(avg)
    print(historiesexittimes)
    return 0
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
            return(render(request,'barcode.html',context))
     
        # val = str(cad.Car_Plate_number)
        # print("Local Registered plate number   "+val)

        # try:
        #     camera=cv2.VideoCapture(0)

        #     while True:
        #         _,Image=camera.read()
        #         cv2.imshow("text recognition",Image)
        #         if cv2.waitKey(1)& 0xFF==ord('s'):
        #             cv2.imwrite('test.jpg',Image)
        #             break
        #     camera.release()
        #     cv2.destroyAllWindows()

            
        #     regions = ['mx', 'us-ca'] # Change to your country
        #     with open('test.jpg', 'rb') as fp:
        #         response = requests.post(
        #             'https://api.platerecognizer.com/v1/plate-reader/',
        #             data=dict(regions=regions),  # Optional
        #             files=dict(upload=fp),
        #             headers={'Authorization': 'Token 6f7ccd3628dcd2d791778bd42d1f3d840f6f0abb'})
        #             #additional token number 'Token 0f1bca95c7fa16cf31122f52ab579db44b41273e'
        #     result=response.json()['results']
        #     res=result[0]
        #     res1=res['plate'].upper()
        #     res2=str(res1)
        #     print("extracted plate number   "+res2)
        #     if res2==val:
        #         print("matched")
        #         print("Card and Car number plate matched")
        #         matchedmsg="Card and Car number plate matched"
        History=history.objects.all()

        if cad.type=='guest':
            print("is guest")

            guest=Guests.objects.get(Card_id=cad.Card_id)
    
            try:
                print("hey")
                if (guest.isentered==False):
                    history.objects.create(Driver_id=guest.Guest_id,Entry_time=datetime.datetime.now(),Card_id=cad)
                    guest.isentered=True
                    guest.save()
                elif guest.isentered==True:
                    if(guest.GuestType=="OneTime"):
                        car=Car.objects.get(Car_Plate_number=guest.Car_Plate_number) #get car detail of that Guest
                        car.delete()
                        cad.delete()
                        guest.delete()
                    else:
                        for hist in History:
                            if (hist.Driver_id==guest.Guest_id):
                                if hist.Exit_time is None:
                                    hist.Exit_time=datetime.datetime.now()
                                    hist.Driver_id=guest.Guest_id
                                    hist.save()
                        guest.isentered=False
                        guest.save()

            except:
                return render(request,'barcode.html',context)
        elif cad.type=='resident':
            print("is resident")
            resident=Residents.objects.get(CNIC=cad.Resident)
            alertOnHistory(cad)
            try:
                print("hey from resident")
                if cad.isentered==False:
                    history.objects.create(Driver_id=resident.Resident_id,Entry_time=datetime.datetime.now(),Card_id=cad)
                    cad.isentered=True
                    cad.save()
                elif cad.isentered==True:
                    for hist in History:
                        if (hist.Card_id==cad):
                            if hist.Exit_time is None:
                                hist.Exit_time=datetime.datetime.now()
                                hist.Driver_id=resident.Resident_id
                                hist.save()
                    cad.isentered=False
                    cad.save()
                                
                # if (resident.isentered==False):
                #     history.objects.create(Driver_id=resident.Resident_id,Entry_time=datetime.datetime.now(),Card_id=cad)
                #     resident.isentered=True
                #     cad.isentered=True
                #     cad.save()
                #     resident.save()
                # elif resident.isentered==True:
                #         if cad.isentered==True:
                #             for hist in History:
                #                 if (hist.Driver_id==resident.Resident_id):
                #                     if hist.Exit_time is None:
                #                         hist.Exit_time=datetime.datetime.now()
                #                         hist.Driver_id=resident.Resident_id
                #                         hist.save()
                #     resident.isentered=False
                #     cad.isentered=False
                #     cad.save()
                #     resident.save()

            except:
                return render(request,'barcode.html',context)

        else:
            print("notmatched")
            print("Car's Number Plate Not Authenticated")
            matchedmsg="Car's Number Plate Not Authenticated"
        context={
                    # "msg":cad.Car_Plate_number,
                    "message":"Card is Registered Against Car Plate Number",
                    # "matched":matchedmsg
                    
                }
        
        return render(request,'barcode.html',context)
    # except:
    #     matchedmsg=""
        
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
    
@login_required(login_url="Login")
def ResidentHistory(request,id):
    resident=Residents.objects.get(Resident_id=id)
    History =history.objects.all()
    context={
        'resident':resident,
        'History':History,
    }
    return render(request,'ResidentHistory.html',context)


#Function to get details of resident from form and save into Resident table 
@login_required(login_url="Login")
def ResidentRegistration(request):
    if request.method=='POST':
        CarNames=[]
        CarNumbers=[]  
        cars=[]
        cards=[]
        F_name=request.POST.get('First_Name')
        L_name=request.POST.get('Last_Name')
        cnic=request.POST.get('CNIC')
        # Car_name=request.POST.get('Car_Name0')
        # cpn=request.POST.get('Car_Plate_number0')
        for x in range(0,100):
            Tag1='Car_Name'+str(x)
            Cn=request.POST.get(Tag1)
            if Cn is not None:
                CarNames.append(Cn)
            Tag2='Car_Plate_number'+str(x)
            cpno=request.POST.get(Tag2)
            if cpno is not None:
                CarNumbers.append(cpno.upper())
        print(CarNames)
        print(CarNumbers)
        # Car_Plate_Number=cpn.upper()
        H_no=request.POST.get('H_no')
        street=request.POST.get('Street')
        sector=request.POST.get('Sector')
        Phone_number=request.POST.get('Phone_Number')
        if 'submitforapproval' in request.POST:
            Residents.objects.create(
                    First_Name=F_name,Last_Name=L_name,CNIC=cnic,
                    Phone_Number=Phone_number,House_no=H_no,Street=street,Sector=sector,type="resident",IsTemporary=True) #save details Resident in table
        else:
            Residents.objects.create(
                    First_Name=F_name,Last_Name=L_name,CNIC=cnic,
                    Phone_Number=Phone_number,House_no=H_no,Street=street,Sector=sector,type="resident") #save details Resident in table
        re=Residents.objects.get(CNIC=cnic)
        for index in range(len(CarNames)):
            bcode=randint(100000000000,999999999999)
            Car.objects.create(Car_Plate_number=CarNumbers[index],Name=CarNames[index]) #save car details of resident in car table
            cars.append(Car.objects.get(Car_Plate_number=CarNumbers[index]))
            Card.objects.create(Car_Plate_number=cars[index],Barcode_id=bcode,type="resident",Resident=re) #save Card details of resident in card table
            abc=Card.objects.get(Car_Plate_number=cars[index])
            print(abc.Resident)
            cards.append(Card.objects.get(Car_Plate_number=cars[index]))
        print(cars)
        print(cards)  
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
                            'car_plate_number':car.Car_Plate_number,
                            'card':card
                    }
    return render(request,'IssueCard.html',context)
@login_required(login_url='Login')
def ViewSpecificResident(request,id):
    re=Residents.objects.get(Resident_id=id)
    card=Card.objects.all()
    context={
                            're':re,
                            'card':card
                    }
    return render(request,'ViewSpecificResident.html',context)
@login_required(login_url='Login')
def issueresidentcard(request,cardid,residentid):
    re=Residents.objects.get(Resident_id=residentid)
    card=Card.objects.get(Card_id=cardid)
    context={
                            'type':'Resident',
                            're':re,
                            'car_name':card.Car_Plate_number.Name,
                            'car_plate_number':card.Car_Plate_number.Car_Plate_number,
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
    
    if request.method=='POST':
        F_name=request.POST.get('First_Name')
        L_name=request.POST.get('Last_Name')
        cnic=request.POST.get('CNIC')
        Car_name=request.POST.get('Car_Name')
        cpn=request.POST.get('Car_Plate_number')
        Car_Plate_Number=cpn.upper()
        H_no=request.POST.get('H_no')
        street=request.POST.get('Street')
        sector=request.POST.get('Sector')
        GuestType=request.POST.get('GuestType')
        bcode=randint(100000000000,999999999999)
        Car.objects.create(Car_Plate_number=Car_Plate_Number,Name=Car_name) #save car details of Guest in car table
        car=Car.objects.get(Car_Plate_number=Car_Plate_Number)
        Card.objects.create(Car_Plate_number=car,Barcode_id=bcode,type="guest")#save Card details of Guest in card table
        
        card=Card.objects.get(Car_Plate_number=Car_Plate_Number)
        Guests.objects.create(
            First_Name=F_name,Last_Name=L_name,CNIC=cnic,
            Card_id=card,Car_Plate_number=car,
            House_no=H_no,Street=street,Sector=sector,type="guest"
            ,GuestType=GuestType
            )#save details Guest in table

        if 'Issuecard' in request.POST:
            re=Guests.objects.get(CNIC=cnic)
            context={
                'type':'Guest',
                    're':re,
                    'car_name':car.Name,
                    'card':card
            }
            return render(request,'IssueCard.html',context)
   

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
    resident=Residents.objects.all()
    car=Car.objects.all()
    card=Card.objects.all()
    context={
        "Residents":resident,
        "car":car,
        "card":card,
    }
    return render(request,'approvalpage.html',context)
@login_required(login_url="Login")
def delete_tempresident(request,id):
    cardss=[]
    cars=[]
    pi=Residents.objects.get(pk=id) #get id of selected resdient entry
    cards=Card.objects.all()
    for card in cards:
        if card.Resident is not None:
            if(card.Resident.CNIC==pi.CNIC):
                cardss.append(card)
    print(cardss)
    for card in cardss:
        car=Car.objects.get(Car_Plate_number=card.Car_Plate_number.Car_Plate_number)
        cars.append(car)
    print(cars)
    for card in cardss:
        card.delete()
    for car in cars:
        car.delete()
    pi.delete()
    resident=Residents.objects.all()   #get all residents
    car=Car.objects.all()              #get all cars
    card=Card.objects.all()            #get all cards
    context={
        "Residents":resident,
        "car":car,
        "card":card,
    }
    return render(request,'approvalpage.html',context)
    pi=temproryresidentdata.objects.get(pk=id) #get id of selected resdient entry  
    pi.delete()
    return redirect('approvalpage')
@login_required(login_url="Login")
def approve_tempresident(request,id):
    pi=Residents.objects.get(pk=id)
    pi.IsTemporary=False
    pi.save()
    return redirect('approvalpage')
@login_required(login_url="Login")
def removecar(request,cardid,residentid):
    card=Card.objects.get(Card_id=cardid)
    car=Car.objects.get(Car_Plate_number=card.Car_Plate_number.Car_Plate_number)
    print(card.Car_Plate_number.Name)
    car.delete()
    card.delete()
    re=Residents.objects.get(Resident_id=residentid)
    card=Card.objects.all()
    context={
        'data':re,
        'card':card
    }
    return render(request,'EditResident.html',context)






