from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login,logout
from django.db.models import Max
from django.contrib.auth.models import User
from .models import ALAA_Form, IdCount, Proposer, Award_Form
import datetime, random, string
from hashlib import sha256
import jwt, mimetypes
from django.core.mail import send_mail

# Create your views here.
jwt_key = "ajsolasjfprapaphsgourhgo"

def alaaform(request):
    if request.method == 'POST':
        token = request.COOKIES.get("jwt")
        jt = jwt.decode(token, jwt_key, algorithms="HS256")
        app_id = jt['app_id']
        user = Proposer.objects.get(app_id=app_id)   
        if Award_Form.objects.filter(app_id=app_id).exists():
            nominee = Award_Form.objects.get(app_id=app_id)
        else:     
            nominee = Award_Form()
        nominee.app_id = app_id
        nominee.award = user.award
        nominee.name = request.POST['name']
        try:
            nominee.gender = request.POST['gender']
        except:
            pass
        try:
            nominee.profile_pic = request.FILES['profile_pic']
        except:
            pass
        nominee.father_name = request.POST['father_name']
        nominee.rollno = request.POST['rollno']
        nominee.dob = request.POST['dob']
        nominee.age = request.POST['age']
        try:
            nominee.degree = request.POST['degree']
        except:
            pass
        try:
            nominee.dept = request.POST['dept']
        except:
            pass
        nominee.yop = request.POST['yop']
        nominee.specialization = request.POST['specialization']
        nominee.mob = request.POST['mob']
        nominee.email = request.POST['email']
        nominee.address = request.POST['address']
        nominee.ppo = request.POST['ppo']
        nominee.distinctions = request.POST['distinctions']
        try:
            nominee.distinctions_file = request.FILES['distinctions_file']
        except:
            pass
        nominee.higher_eduction = request.POST['higher_eduction']
        nominee.professional_exp = request.POST['professional_exp']
        nominee.prof_contri_papers = request.POST['prof_contri_papers']
        try:
            nominee.prof_contri_papers_file = request.FILES['prof_contri_papers_file']
        except:
            pass
        nominee.prof_contri_patents = request.POST['prof_contri_patents']
        try:
            nominee.prof_contri_patents_file = request.FILES['prof_contri_patents_file']
        except:
            pass
        nominee.prof_contri_membership = request.POST['prof_contri_membership']
        try:
            nominee.prof_contri_membership_file = request.FILES['prof_contri_membership_file']
        except:
            pass
        nominee.prof_contri_books = request.POST['prof_contri_books']
        try:
            nominee.prof_contri_books_file = request.FILES['prof_contri_books_file']
        except:
            pass
        nominee.prof_contri_others = request.POST['prof_contri_others']
        try:
            nominee.prof_contri_others_file = request.FILES['prof_contri_others_file']
        except:
            pass
        nominee.prof_hon_award = request.POST['prof_hon_award']
        try:
            nominee.prof_hon_award_file = request.FILES['prof_hon_award_file']
        except:
            pass
        nominee.nom_accom_con = request.POST['nom_accom_con']
        try:
            nominee.nom_accom_con_file = request.FILES['nom_accom_con_file']
        except:
            pass
        nominee.ls1_details = request.POST['ls1_details']
        try:
            nominee.ls1_file = request.FILES['ls1_file']
        except:
            pass
        nominee.ls2_details = request.POST['ls2_details']
        try:
             nominee.ls2_file = request.FILES['ls2_file']
        except:
            pass
        try:
            nominee.resume = request.FILES['resume']
        except:
            pass
        nominee.additional_materials = request.POST['additional_materials']
        try:
            nominee.resume = request.FILES['resume']
        except:
            pass
        #if Award_Form.objects.filter(app_id=app_id).exists():
        nominee.save()
        return redirect('print_pg')
    else:    
        try:
            token = request.COOKIES.get("jwt")
            jt = jwt.decode(token, jwt_key, algorithms="HS256")
        except:
            return redirect("login")
        app_id = jt['app_id']         
        if Award_Form.objects.filter(app_id=app_id).exists():
            user = Award_Form.objects.get(app_id=app_id)
            data = {}
            data['appid'] = user.app_id
            data['award'] = user.award
            data['name'] = user.name
            data['gender'] = user.gender
            data['profile_pic'] = user.profile_pic
            data['father_name'] = user.father_name
            data['rollno'] = user.rollno
            data['dob'] = user.dob
            data['age'] = user.age
            data['degree'] = user.degree
            data['dept'] = user.dept
            data['yop'] = user.yop
            data['specialization'] = user.specialization
            data['mob'] = user.mob
            data['email'] = user.email
            data['address'] = user.address
            data['ppo'] = user.ppo
            data['distinctions'] = user.distinctions
            data['distinctions_file'] = user.distinctions_file
            data['higher_eduction'] = user.higher_eduction
            data['professional_exp'] = user.professional_exp
            data['prof_contri_papers'] = user.prof_contri_papers
            data['prof_contri_papers_file'] = user.prof_contri_papers_file
            data['prof_contri_patents'] = user.prof_contri_patents
            data['prof_contri_patents_file'] = user.prof_contri_patents_file
            data['prof_contri_membership'] = user.prof_contri_membership
            data['prof_contri_membership_file'] = user.prof_contri_membership_file
            data['prof_contri_books'] = user.prof_contri_books
            data['prof_contri_books_file'] = user.prof_contri_books_file
            data['prof_contri_others'] = user.prof_contri_others
            data['prof_contri_others_file'] = user.prof_contri_others_file
            data['prof_hon_award'] = user.prof_hon_award
            data['prof_hon_award_file'] = user.prof_hon_award_file
            data['nom_accom_con'] = user.nom_accom_con
            data['nom_accom_con_file'] = user.nom_accom_con_file
            data['ls1_details'] = user.ls1_details
            data['ls1_file'] = user.ls1_file
            data['ls2_details'] = user.ls2_details
            data['ls2_file'] = user.ls2_file
            data['resume'] = user.resume
            data['additional_materials'] = user.additional_materials
            data['add_file'] = user.add_file
            data['submitted'] =user.submitted
        else: 
            user = Proposer.objects.get(app_id=app_id)
            data = {}
            award = user.award
            data['appid'] = app_id
            data['award'] = award

        response = render(request, 'forms/alaaforms.html', data)
        encoded = jwt.encode({"app_id": app_id}, jwt_key, algorithm="HS256")
        response.set_cookie(key='jwt', value=encoded)
        return response



def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Proposer.objects.filter(app_id=username).exists():
            print("hello")
            user = Proposer.objects.get(app_id=username)
            if user.password == password:
                data = {}
                award = user.award
                data['appid'] = username
                data['award'] = award
                if user.submitted == True:
                    response = redirect('print_pg')
                else:
                    response = redirect('alaaform')
                encoded = jwt.encode({"app_id": username}, jwt_key, algorithm="HS256")
                response.set_cookie(key='jwt', value=encoded)
                return response
            else:
                return render(request,'forms/login.html',{'error': 'Wrong username or password'})

        else:
            return render(request,'forms/login.html',{'error': 'Wrong username or password'})

    else :
        return render(request,'forms/login.html')




    return render(request,'forms/login.html')
    
def register (request):
    if request.method == 'POST':
        #App ID generating
        award_dict = {"For Senior Alumnus: Distinguished Alumnus Award for Professional Excellence (DAAPE)":1 , "For Senior Alumnus: Distinguished Alumnus Award for Public Service (DAAPS)": 2, "For Senior Alumnus: Distinguished Alumnus Award for Service to the NITW/RECW (DAASI)":3, "For Young Alumnus: Distinguished Alumnus Award for Professional Excellence (DAAPE)":4, "For Young Alumnus: Distinguished Alumnus Award for Public Service (DAAPS)":5, "For Young Alumnus: Distinguished Alumnus Award for Service to the NITW/RECW (DAASI)":6, "Alumnus Lifetime Achievement Award":7}
        award = request.POST['award']
        award_id = award_dict[award]
        year = str(datetime.datetime.now().year)
        yy = year[2:]
        uniq_id = IdCount.objects.aggregate(Max('id'))
        uniq_id = uniq_id['id__max'] 
        app_id = str(award_id) + yy + str(uniq_id).zfill(4)

        count = IdCount.objects.get(id=uniq_id)
        count.id = count.id + 1
        count.save()

        #password generating
        password = "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])    
        #print(app_id, password)
        pass_hash = sha256(str.encode(password)).hexdigest()
        proposer = Proposer()
        email = request.POST['email']
        proposer.app_id = app_id
        proposer.password = password
        proposer.name = request.POST['name']
        proposer.mob = request.POST['mob']
        proposer.email = email
        proposer.ppo = request.POST['ppo']
        if Proposer.objects.filter(email = email).exists():
            return redirect('error_404')
        try:
            proposer.alumini = request.POST['alumini']
        except:
            pass
        try:
            proposer.staff = request.POST['staff']
        except:
            pass
        try:
            proposer.something = request.POST['something']
        except:
            pass
        proposer.yop = request.POST['yop']
        proposer.degree = request.POST['degree']
        proposer.dept = request.POST['dept']
        proposer.specialization = request.POST['specialization']
        proposer.award = request.POST['award']
        proposer.address = request.POST['address']
        proposer.save()
        receiver = proposer.email
        sender = "mp841824@student.nitw.ac.in"
        content = "Your Application ID/Username is : " + proposer.app_id
        content = content + "\n Your Password is : " + proposer.password
        content = content + "\n Thanks for Registering."
        content = content + "\n Please don't reply to this Mail-Id."
        rlist = []
        rlist.append(receiver)
        #try:
        #	send_mail('Application Id for Faculty Registration',content,sender,rlist,fail_silently=False,)
        #except BadHeaderError:
        #   return HttpResponse('Invalid header found.')
        #  user = User()
        # user.username = app_id
            #user.password = password
        #  user.email = request.POST['email']
        #  user.save()

        return redirect('user_confirm')
    else:
        return render(request,'forms/register.html')


def print_pg(request):
    if request.method == 'GET':
        try:
            token = request.COOKIES.get("jwt")
            jt = jwt.decode(token, jwt_key, algorithms="HS256")
        except:
            return redirect("login")
        app_id = jt['app_id']         
        user = Award_Form.objects.get(app_id=app_id)
        data = {}
        data['appid'] = user.app_id
        data['award'] = user.award
        data['name'] = user.name
        data['gender'] = user.gender
        data['profile_pic'] = user.profile_pic
        data['father_name'] = user.father_name
        data['rollno'] = user.rollno
        data['dob'] = user.dob
        data['age'] = user.age
        data['degree'] = user.degree
        data['dept'] = user.dept
        data['yop'] = user.yop
        data['specialization'] = user.specialization
        data['mob'] = user.mob
        data['email'] = user.email
        data['address'] = user.address
        data['ppo'] = user.ppo
        data['distinctions'] = user.distinctions
        data['distinctions_file'] = user.distinctions_file
        data['higher_eduction'] = user.higher_eduction
        data['professional_exp'] = user.professional_exp
        data['prof_contri_papers'] = user.prof_contri_papers
        data['prof_contri_papers_file'] = user.prof_contri_papers_file
        data['prof_contri_patents'] = user.prof_contri_patents
        data['prof_contri_patents_file'] = user.prof_contri_patents_file
        data['prof_contri_membership'] = user.prof_contri_membership
        data['prof_contri_membership_file'] = user.prof_contri_membership_file
        data['prof_contri_books'] = user.prof_contri_books
        data['prof_contri_books_file'] = user.prof_contri_books_file
        data['prof_contri_others'] = user.prof_contri_others
        data['prof_contri_others_file'] = user.prof_contri_others_file
        data['prof_hon_award'] = user.prof_hon_award
        data['prof_hon_award_file'] = user.prof_hon_award_file
        data['nom_accom_con'] = user.nom_accom_con
        data['nom_accom_con_file'] = user.nom_accom_con_file
        data['ls1_details'] = user.ls1_details
        data['ls1_file'] = user.ls1_file
        data['ls2_details'] = user.ls2_details
        data['ls2_file'] = user.ls2_file
        data['resume'] = user.resume
        data['additional_materials'] = user.additional_materials
        data['add_file'] = user.add_file
        data['submitted'] =user.submitted

        return render(request,'forms/print_page.html',data)
    else:
        app_id = request.POST['app_id']
        user = Award_Form.objects.get(app_id=app_id)
        data = {}
        data['appid'] = user.app_id
        data['award'] = user.award
        data['name'] = user.name
        data['gender'] = user.gender
        data['profile_pic'] = user.profile_pic
        data['father_name'] = user.father_name
        data['rollno'] = user.rollno
        data['dob'] = user.dob
        data['age'] = user.age
        data['degree'] = user.degree
        data['dept'] = user.dept
        data['yop'] = user.yop
        data['specialization'] = user.specialization
        data['mob'] = user.mob
        data['email'] = user.email
        data['address'] = user.address
        data['ppo'] = user.ppo
        data['distinctions'] = user.distinctions
        data['distinctions_file'] = user.distinctions_file
        data['higher_eduction'] = user.higher_eduction
        data['professional_exp'] = user.professional_exp
        data['prof_contri_papers'] = user.prof_contri_papers
        data['prof_contri_papers_file'] = user.prof_contri_papers_file
        data['prof_contri_patents'] = user.prof_contri_patents
        data['prof_contri_patents_file'] = user.prof_contri_patents_file
        data['prof_contri_membership'] = user.prof_contri_membership
        data['prof_contri_membership_file'] = user.prof_contri_membership_file
        data['prof_contri_books'] = user.prof_contri_books
        data['prof_contri_books_file'] = user.prof_contri_books_file
        data['prof_contri_others'] = user.prof_contri_others
        data['prof_contri_others_file'] = user.prof_contri_others_file
        data['prof_hon_award'] = user.prof_hon_award
        data['prof_hon_award_file'] = user.prof_hon_award_file
        data['nom_accom_con'] = user.nom_accom_con
        data['nom_accom_con_file'] = user.nom_accom_con_file
        data['ls1_details'] = user.ls1_details
        data['ls1_file'] = user.ls1_file
        data['ls2_details'] = user.ls2_details
        data['ls2_file'] = user.ls2_file
        data['resume'] = user.resume
        data['additional_materials'] = user.additional_materials
        data['add_file'] = user.add_file
        data['submitted'] =user.submitted

        return render(request,'forms/print_page.html',data)


def download_file(request):
    try:
        token = request.COOKIES.get("jwt")
        jt = jwt.decode(token, jwt_key, algorithms="HS256")
    except:
        return redirect("login")
    app_id = jt['app_id']         
    file_path = "Nomineefiles/{}/{}".format(app_id, request.filename)

    fl = open(file_path, "r")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    
    return response

def logout(request):
    response = redirect('login')
    response.delete_cookie('jwt')
    return response

def final_submition(request):
    if request.method == 'POST':
        app_id = request.POST['app_id']
        nominee = Award_Form.objects.get(app_id=app_id)
        nominee.submitted = True
        user = Proposer.objects.get(app_id=app_id)
        user.submitted = True
        nominee.save()
        user.save()
        response = redirect('logout')
        return response

def fac_user(request):
    perm = Award_Form.objects.filter(submitted=True)
    data = {}
    data['det'] = []
    for p in perm:
        r = {}
        r['app_id'] = p.app_id
        prop = Proposer.objects.get(app_id=p.app_id)
        r['prop_name'] = prop.name
        r['award'] = p.award
        r['nom_name'] = p.name
        data['det'].append(r)
    return render(request,'forms/fac_user.html', data)

def error_404 (request):
    return render(request,'forms/404.html')

def user_confirm (request):
    return render(request,'forms/user_confirm.html')