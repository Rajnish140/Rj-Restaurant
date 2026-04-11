from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
from django.template import loader
from django.http import HttpResponse
from user.models import Menu

def index(request):
    return render(request,"restaurant.html")


def create_id(request):
    return render(request,"register.html")

def menu(request):
    db=Menu.objects.all().values()
    template=loader.get_template("show_menu.html")

    context={
        'members':db
    }

    return HttpResponse(template.render(context,request))


def datasave(request):
    if request.method == "POST":
        name=request.POST['name']
        mobile = request.POST['mobile']
        password = request.POST['password']
        c_password = request.POST['c_password']

        x=Register(name=name,mobile=mobile,password=password,c_password=c_password)
        x.save()

        #return redirect("/")
def register_p(request):
    return render(request,"register.html")

def register_save(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        x=User.objects.create_user(first_name=fname,last_name=lname,username=mobile)
        x.set_password(password)
        x.save()
        return HttpResponse("success")
    return redirect('/')
def login_page(request):
    return render(request,"login_manager.html")
def login22(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        user=authenticate(username=mobile,password=password)

        if user is None :
            return redirect('login_page')
        else:
            login(request,user)
            return render(request, 'manager.html')

        #try:
        #    user = Manager.objects.get(mobile=mobile, password=password)
        #    # Login manually by storing in session
        #    request.session['manager_id'] = user.id
        #    return render(request, 'manager.html')
        #except Manager.DoesNotExist:
        #    return HttpResponse("failed")

    return render(request, "login_manager.html")       # for x in db:
       #     if x['mobile']==mobile and x['password']==password:
       #         count=count+1
       #         if count>0:
       #            return render(request,'manager.html')   # SUCCESS redirect
       #            #return HttpResponse("Success")
       #     else:
       #         
       #        return HttpResponse("Failed")
       # context={
       # 'msg':"YES"
    
    return HttpResponse(template.render(context,request))


def addmenu(request):
    return render(request,"addmenu.html",{})

# Create your views here.
def addmenu2(request):
    if request.method=="POST":
        dish=request.POST['dish']
        price=request.POST['price']
        number=request.POST['number']

        db=Menu(dish_name=dish,price=price)
        
        db.save()
        if db.save():
            return HttpResponse("Save Successfully")
        else:
            return HttpResponse("failed")

def td(request):
  return render(request,"menu.html")

def showmenu2(request):
  mydata=Menu.objects.all().values()
  template=loader.get_template('update.html')
  context={
    'members':mydata
  }
  return HttpResponse(template.render(context, request))

def id_update(request,id):
    mydata=Menu.objects.get(id=id)
    template=loader.get_template("id_update.html")
    
    context={
        'members':mydata
    }
    return HttpResponse(template.render(context,request))


def save_update(request):
  if request.method=="POST":
    id1=int(request.POST['id'])
    name=request.POST['name']
    price=request.POST['price']

    db=Menu.objects.get(id=id1)
    db.dish_name=name
    db.price=price

    db.save()

    return redirect('../')



def id_delete(request,id):
    mydata=Menu.objects.filter(id=id)
    print(mydata)
    mydata.delete()
    mydata.save()

def show_menu(request):
    db=Menu.objects.all().values()
    template=loader.get_template("menu.html")

    context={
        'members':db
    }

    return HttpResponse(template.render(context,request))

def show_menu2(request):
    db=Menu.objects.filter(dish_name__icontains='Butter').values()
    template=loader.get_template("show_menu.html")

    context={
        'members':db
    }

    return HttpResponse(template.render(context,request))

def order(request):
    d=[]
    d1=[]
    if request.method == "POST":
        checkboxes = request.POST.getlist('check[]')
        quantity = request.POST.getlist('quantity[]')
        customer = request.POST['customer']
        phone = request.POST['mo_number']
        table_no = request.POST['table_no']

         # all selected IDs
         # corresponding quantity
        

        print(quantity)
        list1=[]
        for ch2 in quantity:
            if ch2=="0":
                pass 
            else:
                ch3=int(ch2)
                list1.append(ch3)
        for ch1,li1 in zip(checkboxes,list1):
            data = Menu.objects.filter(id=ch1)
            d = data.values()
            dd=list(d)
            
            
            print(list1)
            len_of_list1=len(list1)
            print(dd)

            for x in (d):
                print(x)
                
                data1 = Order(dish_name=x['dish_name'], price=x['price'],Number_of_plate=li1)
                
                data1.save()
        cs_data=Customer(name=customer,phone=phone,table_no=table_no)
        cs_data.save()
        context={
            'order_data':"Success"
            
        }

        return HttpResponse(context['order_data'])
def orderdata(request):
    db=Order.objects.all().values()
    template=loader.get_template("orderdata.html")

    context={
        'members':db
    }

    return HttpResponse(template.render(context,request))
def bill_page(request):
    if request.method=="POST":
        user=request.POST['user']
        number=request.POST['number']
        table_no=request.POST['table_no']

        # db=Customer.object.get(name=user,phone=number,table_no=table_no)
        # order=Order.object.filter(customer=db)

        template=loader.get_template("bill_page.html")

        context={
            'bill_data':"success"
        }

        return HttpResponse(template.render(context,request))
def contact(request):
    return render("contact")