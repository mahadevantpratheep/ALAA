from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Max
from .models import ALAA_Form, IdCount, Proposer
import datetime, random, string
from hashlib import sha256
# Create your views here.

def alaaform(request):
    if request.method == 'POST' and request.FILES['profile_pic']:
        alaaform = ALAA_Form()
        alaaform.name_proposer = request.POST['name_proposer']
        alaaform.details_proposer = request.POST['details_proposer']
        alaaform.proposer_address = request.POST['proposer_address']
        alaaform.proposer_mob = request.POST['proposer_mob']
        alaaform.proposer_email = request.POST['proposer_email']
        alaaform.name_nominee = request.POST['name_nominee']
        alaaform.nominee_father_name = request.POST['nominee_father_name']
        alaaform.dob = request.POST['dob']
        alaaform.degree = request.POST['degree']
        alaaform.dept = request.POST['dept']
        alaaform.yop = request.POST['yop']
        alaaform.rollno = request.POST['rollno']
        alaaform.otherquali = request.POST['otherquali']
        alaaform.ppo = request.POST['ppo']
        alaaform.nominee_address =  request.POST['nominee_address']
        alaaform.nominee_mob = request.POST['nominee_mob']
        alaaform.nomionee_email =  request.POST['nominee_email']
        alaaform.profile_pic = request.FILES['profile_pic']

        alaaform.save()

        return redirect('alaaform')
    else:
        return render(request,'forms/alaaforms.html')


def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Proposer.objects.filter(app_id=username).exists():
            if Proposer.objects.filter(password=password).exists():
                return render(request,'forms/alaaforms.html')

    else :
        return render(request,'forms/login.html')




    return render(request,'forms/login.html')
    
def register (request):
    if request.method == 'POST':
        #App ID generating
        award_dict = {"award 1":1 , "award 2": 2, "award 3":3, "award 4":4, "award 5":5, "award 6":6, "award 7":7}
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
        print(request.POST)
        proposer = Proposer()
        proposer.app_id = app_id
        proposer.password = password
        proposer.name = request.POST['name']
        proposer.email = request.POST['email']
        proposer.mob = request.POST['mob']
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

        return redirect('login')
    else:
        return render(request,'forms/register.html')