# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Data,Hod
from django.db.models import F,Max

user = ""
huser = ""
year = ""
div = ""
st1=dict()

def index(request):
    global user, st1
    user = ""
    st1={}
    return render(request, 'homepage.html')

def login(request):
    global user,st1
    user=""
    st1={}
    return render(request, 'login.html')

def profile(request):
    global user
    username = request.POST.get('username', 'default')
    password = request.POST.get('password', 'default')
    solution = request.POST.get('solution', 'default')
    soln = solution.casefold()
    bool_answer = Data.objects.filter(login_id=username, password=password, solution=soln).exists()
    mb = Data.objects.filter(president='yes').count()
    #vb1 = Data.objects.all().order_by().values('div').count()
    vb = Data.objects.filter(all_cr_vc=1).count()
    if user == "":
        if bool_answer == True:
            data = Data.objects.filter(login_id=username)
            stu = {
                "dashboard": data,'vb':vb
            }
            user = username
            return render(request, 'profile.html', stu)
        if bool_answer == False:
            return HttpResponse(
                '<script>alert("Please enter valid credentials"); location.assign("login.html"); </script>')
    else:
        data = Data.objects.filter(login_id=user)
        stu = {
            "dashboard": data,'vb':vb
        }
        return render(request, 'profile.html', stu)

    return render(request,'profile.html')

def p_cr_reg(request):
    global user,yes,no
    ans1 = request.POST.get('ans1', 'default')
    ans2 = request.POST.get('ans2', 'default')
    print(ans1, ans2)
    var = Data.objects.get(login_id=user)
    k = Data.objects.filter(year=var.year, div=var.div, dept=var.dept,hod='yes').count()
    print(k)
    if k==2:
        res={'counthod':k}
        return render(request, 'p_cr_reg.html',res)
    if request.POST.get("yes"):
        if var.crformfilled=='yes':
            return HttpResponse(
                '<script>alert("You have already registered"); location.assign("p_cr_reg.html"); </script>')
        elif var.crformfilled=='no':
            return HttpResponse('<script>alert("You have already denied!"); location.assign("p_cr_reg.html"); </script>')
        else:
            Data.objects.filter(login_id=user).update(crformfilled='yes', ans1=ans1, ans2=ans2)
            return HttpResponse(
                '<script>alert("You have succesfully registered"); location.assign("p_cr_reg.html"); </script>')
    elif request.POST.get("no"):
        if var.crformfilled=='yes':
            return HttpResponse(
                '<script>alert("You have already registered. You cannot cancel your registration now!"); location.assign("p_cr_reg.html"); </script>')
        if var.crformfilled=='no':
            return HttpResponse('<script>alert("You have already denied!"); location.assign("p_cr_reg.html"); </script>')
        else:
            return HttpResponse(
                '<script>alert("You registration has been denied by yourself!"); location.assign("p_cr_reg.html"); </script>')
    return render(request, 'p_cr_reg.html')

def pcr_votecount(request):
    global user
    vt = Data.objects.get(login_id=user)
    roll = request.POST.get('rollno', 'default')
    k = Data.objects.filter(year=vt.year, div=vt.div, dept=vt.dept, hod='yes').count()
    h=Data.objects.filter(rollno=roll,hod='yes',year=vt.year,dept=vt.dept,div=vt.div,).exists()
    if h==True:
        if vt.user_vc == 1:
            return HttpResponse('<script>alert("You have already voted!"); location.assign("p_vote_cr.html");</script>')
        else:
            Data.objects.filter(year=vt.year,dept=vt.dept,div=vt.div,rollno=roll).update(vc_pcr=F("vc_pcr") + 1)
            Data.objects.filter(login_id=user).update(user_vc=1)
            return HttpResponse(
                    '<script>alert("Your vote has been counted!"); location.assign("p_vote_cr.html");</script>')
    else:
        return HttpResponse(
            '<script>alert("Please enter the rollno. from the given list!"); location.assign("p_vote_cr.html");</script>')
    return render(request, 'p_vote_cr.html')

def p_vote_cr(request):
    global user
    print(user)
    e = Data.objects.get(login_id=user)
    a = Data.objects.filter(year=e.year, div=e.div, dept=e.dept, hod='yes').exists()
    k = Data.objects.filter(year=e.year, div=e.div, dept=e.dept, hod='yes').count()
    st = {'count': 0}
    print("out", k)
    b = Data.objects.filter(year=e.year, div=e.div, dept=e.dept, hod='yes')
    if k == 2:
        st = {'count': k, 'cr': b}
        mb = Data.objects.filter(div=e.div, dept=e.dept, year=e.year).count()
        vb = Data.objects.filter(dept=e.dept, div=e.div, user_vc=1, year=e.year).count()
        print(mb, vb)
        if mb == vb:
            print("inside k")
            p = Data.objects.filter(div=e.div, dept=e.dept, year=e.year).aggregate(Max('vc_pcr'))
            p1 = p['vc_pcr__max']
            c = Data.objects.get(dept=e.dept, div=e.div, vc_pcr=p1, year=e.year)
            Data.objects.filter(dept=e.dept, div=e.div, year=e.year).update(elected_cr=c.name)
            Data.objects.filter(dept=e.dept, div=e.div, vc_pcr=p1, year=e.year).update(president='yes')
            cc = Data.objects.filter(dept=e.dept, div=e.div, vc_pcr=p1, year=e.year)
            comp = "yes"
            st = {'cr': b, 'pc': cc, 'stud': 'Congratulations! Your CR has been elected', 'count': k, 'comp': comp}
            return render(request, 'p_vote_cr.html', st)
        else:
            print("inside else")
            params = {'cr': b, 'stud': 'Voting is in process...', 'count': k, 'comp': 'no'}
            return render(request, 'p_vote_cr.html', params)

    return render(request, 'p_vote_cr.html',st)

def p_depthead(request):
    global user
    e=Data.objects.get(login_id=user)
    mb=Data.objects.filter(dept=e.dept, year='BE').count()
    vb = Data.objects.filter(dept=e.dept, user_vc=1, year='BE').count()
    if mb==vb:
        g = Data.objects.filter(dept=e.dept, year='BE').aggregate(Max('vc_pcr'))
        g1 = g['vc_pcr__max']
        h = Data.objects.get(dept=e.dept, vc_pcr=g1, year='BE')
        Data.objects.filter(dept=e.dept).update(elected_dept_head=h.name)
        hh = Data.objects.filter(dept=e.dept, vc_pcr=g1,year='BE')
        st1 = {'gc': hh}
        return render(request, 'p_depthead.html', st1)
    else:
        return HttpResponse('<script>alert("Voting is still in process. Please wait!"); location.assign("profile.html"); </script>')
    return render(request, 'p_depthead.html', st1)

def p_president_interview(request):
    global user
    e=Data.objects.get(login_id=user)
    ans = request.POST.get('ans')
    if request.POST.get("interview"):
        if e.name==e.elected_dept_head and e.year=='BE':
            y=Data.objects.filter(name=e.elected_dept_head,ans__isnull=True,year='BE').exists()
            if y == True:
                Data.objects.filter(name=e.elected_dept_head, year='BE').update(ans=ans)
                return HttpResponse(
                    '<script>alert("You have successfully submitted the form!"); location.assign("p_president_interview.html");</script>')
            else:
                return HttpResponse(
                    '<script>alert("You have already filled this form"); location.assign("p_president_interview.html");</script>')

        else:
            return HttpResponse('<script>alert("Only elected dept heads are eligible to fill this interview form!"); location.assign("profile.html");</script>')
    m = Data.objects.order_by().values('dept').distinct().count()
    v = Data.objects.filter(ans__isnull=False).count()
    if m == v:
        p = Data.objects.all().filter(ans__isnull=False).values('ans').distinct()
        q = Data.objects.all().filter(ans__isnull=False).values('id').distinct()
        p1 = list(p)
        p2 = [x['ans'] for x in p1]
        q1 = list(q)
        q2 = [y['id'] for y in q1]
        r = zip(p2, q2)
        #bar graph
        q = Data.objects.all().filter(ans__isnull=False).values('name')
        p = Data.objects.all().filter(ans__isnull=False).values('s_dept_vc')
        q1 = list(q)
        q2 = [y['name'] for y in q1]
        p1 = list(p)
        p2 = [y['s_dept_vc'] for y in p1]

        st9 = {
            'r': r, 'countans': 'yes', 'abc':e.dept_vc,'pollst': q2, 'pollvotes': p2
        }
        ans1 = request.POST.get('answer')
        if request.POST.get("idbut"):
            if e.dept_vc == 1:

                return HttpResponse(
                    '<script>alert("You have already voted!"); location.assign("p_president_interview.html");</script>')
            else:
                Data.objects.filter(id=ans1).update(s_dept_vc=F("s_dept_vc") + 1)
                Data.objects.filter(login_id=user).update(dept_vc=1)

                return HttpResponse(
                    '<script>alert("Your vote has been counted!"); location.assign("p_president_interview.html");</script>')
        return render(request, 'p_president_interview.html',st9 )
    return render(request, 'p_president_interview.html')

def p_poll(request):
    global user
    e=Data.objects.get(login_id=user)
    mb = Data.objects.all().count()
    vb = Data.objects.filter(dept_vc=1).count()
    if mb == vb:
        if e.all_cr_vc == 1:
            comp1="yes"
            print("allcrvs")
            s2 = Data.objects.order_by('-s_dept_vc')[1]
            s1 = Data.objects.order_by('-s_dept_vc')[0]
            pre1 = Data.objects.get(name=s1, year=s1.year)
            pre2 = Data.objects.get(name=s2, year=s2.year)
            st4 = {'labels': [pre1.name, pre2.name], 'data': [pre1.cr_vc, pre2.cr_vc],'xyz': e.all_cr_vc, 'comp1': comp1}

            return render(request, 'p_poll.html', st4)
        else:
            print("elseeeeee")
            comp1 = "yes"
            s2 = Data.objects.order_by('-s_dept_vc')[1]
            s1 = Data.objects.order_by('-s_dept_vc')[0]
            ss1=Data.objects.filter(name=s1, year='BE')
            ss2=Data.objects.filter(name=s2, year='BE')
            st4 = {'ss1': ss1, 'ss2': ss2, 'comp1' : comp1, 'stud': 'These are your 2 selected candidates for presidential election:'}
            print(st4)
            return render(request, 'p_poll.html', st4)
    return render(request,'p_poll.html')

def p_final(request):
    global user
    e=Data.objects.get(login_id=user)
    fin=request.POST.get('fin')
    h = Data.objects.filter(id=fin, hod='yes', year=e.year).exists()
    if h == True:
        if e.name==e.elected_cr:
                if request.POST.get("final"):
                    if e.all_cr_vc==1:
                        return HttpResponse(
                            '<script>alert("You have already voted!"); location.assign("p_poll.html");</script>')
                    else:
                        Data.objects.filter(id=fin).update(cr_vc=F("cr_vc") + 1)
                        Data.objects.filter(login_id=user).update(all_cr_vc=1)
                        return HttpResponse(
                            '<script>alert("Your vote has been counted!"); location.assign("p_poll.html");</script>')
        else:
            return HttpResponse(
                    '<script>alert("You are not eligible to vote for president!"); location.assign("p_poll.html");</script>')
    else:
        return HttpResponse(
            '<script>alert("Please enter the id displayed below!"); location.assign("p_poll.html");</script>')
    return render(request, 'p_poll.html')

def p_final_president(request):
    global user
    e = Data.objects.get(login_id=user)
    mb = Data.objects.filter(president='yes').count()
    vb = Data.objects.all().filter(all_cr_vc=1).count()

    print(mb)
    print(vb)
    if mb == vb:

        s2 = Data.objects.order_by('-cr_vc')[0]
        f=Data.objects.filter(name=s2, year='BE')
        st5={
            'f':f,'vb':vb
        }
        print(st5)
        return render(request, 'p_final_president.html', st5)
    else:
        return HttpResponse(
            '<script>alert("Voting is still in process. Please wait!"); location.assign("profile.html"); </script>')
    return render(request,'p_final_president.html',st5)


def results(request):
    # one table for cr(name,year,div,dept,roll no) dept heads(name,year,div,dept)
    r = Data.objects.all().order_by().values('elected_cr').distinct()
    s = Data.objects.all().order_by().values('elected_dept_head').distinct()
    t = Data.objects.filter(div__isnull=False, year__isnull=False, dept__isnull=False).order_by('vc_pcr')[0]
    print("This is t", t)
    rs = []
    r1 = list(r)
    r2 = [x['elected_cr'] for x in r1]
    rs1 = []
    s1 = list(s)
    s2 = [x['elected_dept_head'] for x in s1]

    for i in r2:
        sss = Data.objects.filter(name=i, elected_cr=i)
        rs.append(sss)

    for j in s2:
        rrr = Data.objects.filter(name=j, elected_dept_head=j, year='BE')
        rs1.append(rrr)

    mb = Data.objects.filter(president='yes').count()
    vb = Data.objects.filter(all_cr_vc=1).count()

    if mb == vb:
        result = {'r': rs, 's': rs1}
        return render(request, 'results.html', result)
    else:
        resu={'res':'no'}
        print(resu)
        return render(request, 'results.html', resu)
    return render(request, 'results.html', result)

def hod_login(request):
    global huser
    huser = ""
    return render(request, 'hod_login.html')



def display(request):
    global huser,year,div
    year = request.POST.get('year', 'default')
    div = request.POST.get('div', 'default')
    d = Hod.objects.get(hod_login_id=huser)
    check = Data.objects.filter(year=year, div=div, dept=d.dept).exists()

    if check == True:
        find = Data.objects.filter(year=year, div=div, crformfilled='yes',dept=d.dept)
        print(find)
        find1 = {'find':find, 'year':year, 'div':div, 'dept':d.dept,'done':'no'}

        id1 = request.POST.get('id1')
        id2 = request.POST.get('id2')
        chk1 = Data.objects.filter(hod__isnull=False,year=year,div=div,dept=d.dept).count()
        if chk1 == 2:
            return render(request,'display.html',{'done':'yes','year':year,'div':div,'dept':d.dept})
        else:
            cd1 = Data.objects.filter(id=id1).update(hod='yes')
            cd2 = Data.objects.filter(id=id2).update(hod='yes')
            print("bakiiiiii")
        return render(request, 'display.html',find1)
    return render(request, 'display.html')

def dn(request):
    global huser,year,div
    d = Hod.objects.get(hod_login_id=huser)
    id1 = request.POST.get('id1')
    id2 = request.POST.get('id2')

    cd1 = Data.objects.filter(id=id1).update(hod='yes')
    cd2 = Data.objects.filter(id=id2).update(hod='yes')
    print('button')
    print(id1, id2)
    return render(request, 'display.html',{'year':year,'div':div,'dept':d.dept,'done':'yes'})

def hod_trial(request):
    global huser
    username = request.POST.get('username', 'default')
    password = request.POST.get('password', 'default')
    b = Hod.objects.filter(hod_login_id=username, hod_password=password).exists()
    if huser=="":
        if b == True:
            huser=username
            return render(request, 'hod_trial.html')
    else:
        if b == True:
            c = Data.objects.order_by().values('div').distinct()
            c1 = Data.objects.order_by().values('year').distinct()
            s = []
            r1 = list(c)
            r2 = [x['div'] for x in r1]
            for i in r2:
                s.append(i)

            s1 = []
            r11 = list(c1)
            r22 = [x['year'] for x in r11]
            for i in r22:
                s1.append(i)
            print(s1)
            h = {'s': s, 's1': s1}
            return render(request, 'hod_trial.html', h)
        else:
            return HttpResponse(
                '<script>alert("Please enter valid credentials"); location.assign("hod_login.html"); </script>')
    return render(request, 'hod_trial.html')

def knowtheprocess(request):
    return render(request,'knowtheprocess.html')