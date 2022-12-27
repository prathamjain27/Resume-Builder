from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from . models import Res0,Res1, Pg0, Pg1

def index0(request):
    return render(request, 'index0.html')

def gra_res(request):
    return render(request, 'gra_res.html')

def pg_res(request):
    return render(request, 'pg_res.html')
        
def res_form0(request):
    if request.method=="POST":
        name=request.POST['name']
        new_name=Res0(name = name)
        new_name.save()
        name=request.POST['name']
        title=request.POST['title']
        phone=request.POST['phone']
        email=request.POST['email']
        s1=request.POST['s1']
        s2=request.POST['s2']
        s3=request.POST['s3']
        s4=request.POST['s4']
        l1=request.POST['l1']
        l2=request.POST['l2']
        l3=request.POST['l3']
        about=request.POST['about']
        year10=request.POST['year10']
        school10=request.POST['school10']
        place10=request.POST['place10']
        board10=request.POST['board10']
        per10=request.POST['per10']
        year12=request.POST['year12']
        school12=request.POST['school12']
        place12=request.POST['place12']
        board12=request.POST['board12']
        per12=request.POST['per12']
        yearg=request.POST['yearg']
        institute=request.POST['institute']
        placeg=request.POST['placeg']
        degree=request.POST['degree']
        perg=request.POST['perg']
        dob=request.POST['dob']
        gender=request.POST['gender']
        father=request.POST['father']
        mother=request.POST['mother']
        nation=request.POST['nation']
        h1=request.POST['h1']
        h2=request.POST['h2']
        h3=request.POST['h3']
        h4=request.POST['h4']
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']      
        
        return render(request, "resume0.html", {'name': name, 'title' :title, 'phone': phone, 'email':email, 's1':s1, 's2':s2,'s3':s3, 's4':s4, 
            'l1':l1, 'l2':l2, 'l3':l3, 'about':about, 'year10':year10, 'school10': school10, 'place10': place10, 'board10': board10, 'per10' : per10,
            'year12':year12, 'school12': school12, 'place12': place12, 'board12': board12, 'per12' : per12, 'yearg':yearg, 'institute': institute, 
            'placeg': placeg, 'degree':degree, 'perg' : perg,'dob':dob, 'gender':gender,'father':father,'mother':mother,'nation':nation,'h1':h1, 
            'h2':h2,'h3':h3, 'h4':h4, 'p1':p1,'p2':p2, 'p3':p3, })
    
    elif request.method=='GET':
        return render(request, 'res_form0.html')
    else:
        return HttpResponse('error')

def res_form1(request):
    if request.method=="POST":
        name=request.POST['name']
        new_name=Res1(name = name)
        new_name.save()
        name=request.POST['name']
        title=request.POST['title']
        phone=request.POST['phone']
        email=request.POST['email']
        s1=request.POST['s1']
        s2=request.POST['s2']
        s3=request.POST['s3']
        s4=request.POST['s4']
        l1=request.POST['l1']
        l2=request.POST['l2']
        l3=request.POST['l3']
        about=request.POST['about']
        year10=request.POST['year10']
        school10=request.POST['school10']
        place10=request.POST['place10']
        board10=request.POST['board10']
        per10=request.POST['per10']
        year12=request.POST['year12']
        school12=request.POST['school12']
        place12=request.POST['place12']
        board12=request.POST['board12']
        per12=request.POST['per12']
        yearg=request.POST['yearg']
        institute=request.POST['institute']
        placeg=request.POST['placeg']
        degree=request.POST['degree']
        perg=request.POST['perg']
        dob=request.POST['dob']
        gender=request.POST['gender']
        father=request.POST['father']
        mother=request.POST['mother']
        nation=request.POST['nation']
        h1=request.POST['h1']
        h2=request.POST['h2']
        h3=request.POST['h3']
        h4=request.POST['h4']
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']      
        
        return render(request, "resume1.html", {'name': name, 'title' :title, 'phone': phone, 'email':email, 's1':s1, 's2':s2,'s3':s3, 's4':s4, 
            'l1':l1, 'l2':l2, 'l3':l3, 'about':about, 'year10':year10, 'school10': school10, 'place10': place10, 'board10': board10, 'per10' : per10,
            'year12':year12, 'school12': school12, 'place12': place12, 'board12': board12, 'per12' : per12, 'yearg':yearg, 'institute': institute, 
            'placeg': placeg, 'degree':degree, 'perg' : perg,'dob':dob, 'gender':gender,'father':father,'mother':mother,'nation':nation,'h1':h1, 
            'h2':h2,'h3':h3, 'h4':h4, 'p1':p1,'p2':p2, 'p3':p3, })

    elif request.method=='GET':
        return render(request, 'res_form1.html')
    else:
        return HttpResponse('error')


def pg_res_form0(request):
    if request.method=="POST":
        name=request.POST['name']
        new_name=Pg0(name = name)
        new_name.save()
        name=request.POST['name']
        title=request.POST['title']
        phone=request.POST['phone']
        email=request.POST['email']
        s1=request.POST['s1']
        s2=request.POST['s2']
        s3=request.POST['s3']
        s4=request.POST['s4']
        l1=request.POST['l1']
        l2=request.POST['l2']
        l3=request.POST['l3']
        about=request.POST['about']
        year10=request.POST['year10']
        school10=request.POST['school10']
        place10=request.POST['place10']
        board10=request.POST['board10']
        per10=request.POST['per10']
        year12=request.POST['year12']
        school12=request.POST['school12']
        place12=request.POST['place12']
        board12=request.POST['board12']
        per12=request.POST['per12']
        yearg=request.POST['yearg']
        institute=request.POST['institute']
        placeg=request.POST['placeg']
        degree=request.POST['degree']
        perg=request.POST['perg']
        yearpg=request.POST['yearpg']
        institutepg=request.POST['institutepg']
        placepg=request.POST['placepg']
        degreepg=request.POST['degreepg']
        perpg=request.POST['perpg']
        dob=request.POST['dob']
        gender=request.POST['gender']
        father=request.POST['father']
        mother=request.POST['mother']
        nation=request.POST['nation']
        h1=request.POST['h1']
        h2=request.POST['h2']
        h3=request.POST['h3']
        h4=request.POST['h4']
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3'] 
        
        return render(request, "pg_resume0.html", {'name': name, 'title' :title, 'phone': phone, 'email':email, 's1':s1, 's2':s2,
         's3':s3, 's4':s4, 'l1':l1, 'l2':l2, 'l3':l3, 'about':about, 'year10':year10, 'school10': school10, 'place10': place10, 'board10': board10, 'per10' : per10,
         'year12':year12, 'school12': school12, 'place12': place12, 'board12': board12, 'per12' : per12, 'yearg':yearg, 'institute': institute, 'placeg': placeg, 'degree': degree, 'perg' : perg,
         'yearpg':yearpg, 'institutepg': institutepg, 'placepg': placepg, 'degreepg': degreepg, 'perpg' : perpg, 'dob':dob, 'gender':gender,'father':father,'mother':mother,'nation':nation,'h1':h1, 
        'h2':h2,'h3':h3, 'h4':h4, 'p1':p1,'p2':p2, 'p3':p3,})
    
    elif request.method=='GET':
        return render(request, 'pg_res_form0.html')
    else:
        return HttpResponse('error')

def pg_res_form1(request):
    if request.method=="POST":
        name=request.POST['name']
        new_name=Pg1(name = name)
        new_name.save()
        name=request.POST['name']
        title=request.POST['title']
        phone=request.POST['phone']
        email=request.POST['email']
        s1=request.POST['s1']
        s2=request.POST['s2']
        s3=request.POST['s3']
        s4=request.POST['s4']
        l1=request.POST['l1']
        l2=request.POST['l2']
        l3=request.POST['l3']
        about=request.POST['about']
        year10=request.POST['year10']
        school10=request.POST['school10']
        place10=request.POST['place10']
        board10=request.POST['board10']
        per10=request.POST['per10']
        year12=request.POST['year12']
        school12=request.POST['school12']
        place12=request.POST['place12']
        board12=request.POST['board12']
        per12=request.POST['per12']
        yearg=request.POST['yearg']
        institute=request.POST['institute']
        placeg=request.POST['placeg']
        degree=request.POST['degree']
        perg=request.POST['perg']
        yearpg=request.POST['yearpg']
        institutepg=request.POST['institutepg']
        placepg=request.POST['placepg']
        degreepg=request.POST['degreepg']
        perpg=request.POST['perpg']
        dob=request.POST['dob']
        gender=request.POST['gender']
        father=request.POST['father']
        mother=request.POST['mother']
        nation=request.POST['nation']
        h1=request.POST['h1']
        h2=request.POST['h2']
        h3=request.POST['h3']
        h4=request.POST['h4']
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']
        
        
        return render(request, "pg_resume1.html", {'name': name, 'title' :title, 'phone': phone, 'email':email, 's1':s1, 's2':s2,
         's3':s3, 's4':s4, 'l1':l1, 'l2':l2, 'l3':l3, 'about':about, 'year10':year10, 'school10': school10, 'place10': place10, 'board10': board10, 'per10' : per10,
         'year12':year12, 'school12': school12, 'place12': place12, 'board12': board12, 'per12' : per12, 'yearg':yearg, 'institute': institute, 'placeg': placeg, 'degree': degree, 'perg' : perg,
         'yearpg':yearpg, 'institutepg': institutepg, 'placepg': placepg, 'degreepg': degreepg, 'perpg' : perpg,'dob':dob, 'gender':gender,'father':father,'mother':mother,'nation':nation,'h1':h1, 
        'h2':h2,'h3':h3, 'h4':h4, 'p1':p1,'p2':p2, 'p3':p3,})
    
    elif request.method=='GET':
        return render(request, 'pg_res_form1.html')
    else:
        return HttpResponse('error')

def resume0(request):
    return render(request, 'resume0.html')

def resume1(request):
    return render(request, 'resume1.html')

def pg_resume0(request):
    return render(request, 'pg_resume0.html')

def pg_resume1(request):
    return render(request, 'pg_resume1.html')