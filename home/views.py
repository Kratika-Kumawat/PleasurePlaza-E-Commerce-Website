from django.shortcuts import render
from .models import Product, Mobile, Television, Air_Conditioner, Washing_Machine, Refrigerator, Laptop, Headphones, Camera, Tablets, Books, Fashion
import random


def main(request):
    # Mobiles
    m = Mobile.objects.all()
    M = []
    for i in range(0, len(m), 5):
        M.append(m[i:i+5])

    # fashion
    f = Fashion.objects.all()
    F = []
    for i in range(0, len(f), 5):
        F.append(f[i:i+5])

    # laptops
    l = Laptop.objects.all()
    L = []
    for i in range(0, len(l), 5):
        L.append(l[i:i+5])

    # tv
    t = Television.objects.all()
    T = []
    for i in range(0, len(t), 5):
        T.append(t[i:i+5])

    # headphones
    h = Headphones.objects.all()
    H = []
    for i in range(0, len(h), 5):
        H.append(h[i:i+5])

    # washing machines
    w = Washing_Machine.objects.all()
    W = []
    for i in range(0, len(w), 5):
        W.append(w[i:i+5])

    # refrigerators
    r = Refrigerator.objects.all()
    R = []
    for i in range(0, len(r), 5):
        R.append(r[i:i+5])

    # AC
    a = Air_Conditioner.objects.all()
    A = []
    for i in range(0, len(a), 5):
        A.append(a[i:i+5])

    # Tablets
    tab = Tablets.objects.all()
    Tab = []
    for i in range(0, len(tab), 5):
        Tab.append(tab[i:i+5])

    # camera
    c = Camera.objects.all()
    C = []
    for i in range(0, len(c), 5):
        C.append(c[i:i+5])

    # books
    b = Books.objects.all()
    B = []
    for i in range(0, len(b), 5):
        B.append(b[i:i+5])

    data = {
        "m1": M[0], "m2": M[1:],
        "f1": F[0], "f2": F[1:],
        "l1": L[0], "l2": L[1:],
        "t1": T[0], "t2": T[1:],
        "h1": H[0], "h2": H[1:],
        "w1": W[0], "w2": W[1:],
        "r1": R[0], "r2": R[1:],
        "a1": A[0], "a2": A[1:],
        "tab1": Tab[0], "tab2": Tab[1:],
        "c1": C[0], "c2": C[1:],
        "b1": B[0], "b2": B[1:]
    }

    return render(request, "main.html", data)

def rating(x):
    a=[]
    for i in range(len(x)):
        a.append(random.randint(10000,90000))
    return a

def review(x):
    a=[]
    for i in range(len(x)):
        a.append(random.randint(1000,10000))
    return a

def highlights(x):
    y=x.values()
    a=[]
    for i in range(len(y)):
        b=dict(y[i])
        z=b['highlights']
        a.append(z.split('\n'))
    # print(a)
    return a

def offer(x):
    a=[]
    for i in range(len(x)):
        a.append(random.randint(5,55))    
    return a

def total_price(o,x):
    # print(o)
    y=x.values()
    a=[]
    for i in range(len(y)):
        b=dict(y[i])
        z=b['price']
        # print(z)
        z=int(z)
        s=(z*100)//(100-o[i])
        a.append(s)
    print(a)
    return a

def mobile(request):
    pro = Mobile.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)
    return render(request, "mobile.html", {'mobile': pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})


def laptop(request):
    pro = Laptop.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)
    return render(request, "laptop.html", {'laptop':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})
    
def television(request):
    pro = Television.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro) 
    return render(request, "television.html", {'tv':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})
    
    
def washing_machine(request):
    pro=Washing_Machine.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)  
    return render(request, "washing_mach.html", {'wm':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})

def refrigerator(request):
    pro=Refrigerator.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)   
    return render(request, "refrigerator.html", {'ref':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})


def air_conditioners(request):
    pro=Air_Conditioner.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)  
    return render(request, "ac.html", {'ac':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})

def tablets(request):
    pro= Tablets.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro) 
    return render(request, "tab.html", {'tab':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})

def camera(request):
    pro=Camera.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro) 
    return render(request, "camera.html", {'cam':pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})

def fashion(request,cat):
    if cat=="all":
        pro=Fashion.objects.all()
        print(pro)
        # print(pro[0])
        # r1=rating(pro)
        # r2=review(pro)
        # # h=highlights(pro)
        o=offer(pro)
        t=total_price(o,pro) 
        # return render(request, "Fashion.html", {'cam':pro,'r1':r1,'r2':r2,'o':o,'t':t})
        return render(request,"fashion.html",{'f': pro,'o':o,'t':t})
    elif cat=="Men":
        f=Fashion.objects.filter(gender=cat)
        o=offer(f)
        t=total_price(o,f) 
        # return render(request, "Fashion.html", {'cam':pro,'r1':r1,'r2':r2,'o':o,'t':t})
        return render(request,"fashion.html",{'f': f,'o':o,'t':t})
    elif cat=="Women":
        f=Fashion.objects.filter(gender=cat)
        o=offer(f)
        t=total_price(o,f) 
        # return render(request, "Fashion.html", {'cam':pro,'r1':r1,'r2':r2,'o':o,'t':t})
        return render(request,"fashion.html",{'f': f,'o':o,'t':t})
    else:
        f=Fashion.objects.filter(gender=cat)
        o=offer(f)
        t=total_price(o,f) 
        # return render(request, "Fashion.html", {'cam':pro,'r1':r1,'r2':r2,'o':o,'t':t})
        return render(request,"fashion.html",{'f': f,'o':o,'t':t})
        
    
def books(request):
    pro=Books.objects.all()
    # r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro) 
    return render(request, "books.html", {'book':pro,'r2':r2,'h':h,'o':o,'t':t})

def headphones(request):
    pro = Headphones.objects.all()
    r1=rating(pro)
    r2=review(pro)
    h=highlights(pro)
    o=offer(pro)
    t=total_price(o,pro)
    return render(request, "headphones.html", {'hp': pro,'r1':r1,'r2':r2,'h':h,'o':o,'t':t})

def mobilead(request):
    m = Mobile.objects.all()
    M = []
    for i in range(0, len(m), 5):
        M.append(m[i:i+5])
    data = {
        "m1": M[0], "m2": M[1:]
    }
    return render(request, "mobilead.html",data)

def fashionad(request):
    cat1="Men"
    cat2="Women"
    cat3="Kids"
    f=Fashion.objects.filter(gender=cat1)
    f1=Fashion.objects.filter(gender=cat2)
    f2=Fashion.objects.filter(gender=cat3)
    print(f)
    return render(request, "fashionad.html",{'men':f,'wmen':f1,'kid':f2})

def electronicad(request):
    h = Headphones.objects.all()
    H = []
    for i in range(0, len(h), 5):
        H.append(h[i:i+5])
    l = Laptop.objects.all()
    L = []
    for i in range(0, len(l), 5):
        L.append(l[i:i+5])
    tab = Tablets.objects.all()
    Tab = []
    for i in range(0, len(tab), 5):
        Tab.append(tab[i:i+5])
    c = Camera.objects.all()
    C = []
    for i in range(0, len(c), 5):
        C.append(c[i:i+5])
    return render(request, "electronicad.html",{"h1": H[0], "h2": H[1:],"l1": L[0], "l2": L[1:],"tab1": Tab[0], "tab2": Tab[1:],"c1": C[0], "c2": C[1:]})

def appad(request):
    t = Television.objects.all()
    T = []
    for i in range(0, len(t), 5):
        T.append(t[i:i+5])
    w = Washing_Machine.objects.all()
    W = []
    for i in range(0, len(w), 5):
        W.append(w[i:i+5])
    r = Refrigerator.objects.all()
    R = []
    for i in range(0, len(r), 5):
        R.append(r[i:i+5])
    a = Air_Conditioner.objects.all()
    A = []
    for i in range(0, len(a), 5):
        A.append(a[i:i+5])
    c = Camera.objects.all()
    C = []
    for i in range(0, len(c), 5):
        C.append(c[i:i+5])
    return render(request, "appad.html",{"t1": T[0], "t2": T[1:],"w1": W[0], "w2": W[1:],"r1": R[0], "r2": R[1:],"a1": A[0], "a2": A[1:],"c1": C[0], "c2": C[1:]})