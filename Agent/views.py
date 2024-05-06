from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.

def homepage(request):
    if 'sid' in request.session:
        return render(request,"Agent/HomePage.html")
    else:
        return redirect("Guest:Login")

def my_pro(request):
    if 'sid' in request.session:
        data=tbl_agent.objects.get(id=request.session["sid"])
        return render(request,"Agent/MyProfile.html",{'data':data})
    else:
        return redirect("Guest:Login")


def editprofile(request):
    prodata=tbl_agent.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.agent_name=request.POST.get('txtname')
        prodata.agent_contact=request.POST.get('txtcon')
        prodata.agent_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Agent/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Agent/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_agent.objects.filter(id=request.session["sid"],agent_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                agentdata=tbl_agent.objects.get(id=request.session["sid"],agent_password=request.POST.get('txtcurpass'))
                agentdata.agent_password=request.POST.get('txtnewpass')
                agentdata.save()
                return render(request,"Agent/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Agent/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Agent/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Agent/ChangePassword.html")

def vieworders(request):
    if 'sid' in request.session:
        swap = tbl_swap.objects.filter(swap_paymentstatus__lte=2,swap_status=0)
        agentid = tbl_agent.objects.get(id=request.session["sid"])
        utou = tbl_ubooking.objects.filter(booking_status__gte=2)
        ptou = tbl_booking.objects.filter(booking_status__gte=2)
        return render(request,"Agent/ViewOrders.html",{"swaping":swap,"agent":agentid,"utou":utou,"ptou":ptou})
    else:
        return redirect("Guest:Login")


def take_order(request,id):
    if 'sid' in request.session:
        swap = tbl_swap.objects.get(id=id)
        swap.swap_status = 1
        swap.agent = tbl_agent.objects.get(id=request.session["sid"])
        swap.save()
        return redirect("Agent:vieworders")
    else:
        return redirect("Guest:Login")


def order_collected(request,id):
    if 'sid' in request.session:
        swap = tbl_swap.objects.get(id=id)
        swap.swap_status = 2
        swap.save()
        return redirect("Agent:vieworders")
    else:
        return redirect("Guest:Login")


def order_delivered(request,id):
    if 'sid' in request.session:
        swap = tbl_swap.objects.get(id=id)
        swap.swap_status = 3
        swap.save()
        return redirect("Agent:vieworders")
    else:
        return redirect("Guest:Login")


def order_returned(request,id):
    if 'sid' in request.session:
        swap = tbl_swap.objects.get(id=id)
        swap.swap_status = 4
        swap.save()
        return redirect("Agent:vieworders")
    else:
        return redirect("Guest:Login")

def returned_delivered(request,id):
    if 'sid' in request.session:
        swap = tbl_swap.objects.get(id=id)
        swap.swap_status = 5
        swap.save()
        return redirect("Agent:vieworders")
    else:
        return redirect("Guest:Login")
    
def viewproduct(request,id):
    cartpdt = tbl_ucart.objects.filter(booking=id)
    return render(request,"Agent/View_products.html",{"data":cartpdt})

def viewpublisherproduct(request,id):
    cartpdt = tbl_cart.objects.filter(booking=id)
    return render(request,"Agent/View_Publisher_Product.html",{"data":cartpdt})

def myorders(request):
    swap = tbl_swap.objects.filter(swap_paymentstatus__gt=1,agent=request.session["sid"])
    utou = tbl_ubooking.objects.filter(booking_status__gte=2,agent=request.session["sid"])
    ptou = tbl_booking.objects.filter(booking_status__gte=2,agent=request.session["sid"])
    agentid = tbl_agent.objects.get(id=request.session["sid"])
    return render(request,"Agent/My_orders.html",{"swaping":swap,"utou":utou,"ptou":ptou,"agent":agentid})

def getutouorder(request,id):
    if 'sid' in request.session:
        swap = tbl_ubooking.objects.get(id=id)
        swap.booking_status = 3
        swap.agent = tbl_agent.objects.get(id=request.session["sid"])
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")
    
def getptouorder(request,id):
    if 'sid' in request.session:
        swap = tbl_booking.objects.get(id=id)
        swap.booking_status = 3
        swap.agent = tbl_agent.objects.get(id=request.session["sid"])
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")

def collect_utou_order(request,id):
    if 'sid' in request.session:
        swap = tbl_ubooking.objects.get(id=id)
        swap.booking_status = 4
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")
    
def delivered_utou_order(request,id):
    if 'sid' in request.session:
        swap = tbl_ubooking.objects.get(id=id)
        swap.booking_status = 5
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")
    
def collect_ptou_order(request,id):
    if 'sid' in request.session:
        swap = tbl_booking.objects.get(id=id)
        swap.booking_status = 4
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")
    
def delivered_ptou_order(request,id):
    if 'sid' in request.session:
        swap = tbl_booking.objects.get(id=id)
        swap.booking_status = 5
        swap.save()
        return redirect("Agent:myorders")
    else:
        return redirect("Guest:Login")

def logout(request):
    del request.session['sid']
    return redirect("Guest:Login")