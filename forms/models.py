from django.db import models
from django.core.validators import FileExtensionValidator
from .path import *
# Create your models here.

def get_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, filename)

class IdCount(models.Model):
    id = models.IntegerField(primary_key=True)

class Proposer(models.Model):
    app_id =  models.IntegerField()
    password = models.CharField(max_length = 255)
    name = models.CharField(max_length = 63)
    email = models.EmailField()
    mob = models.CharField(max_length = 63)
    alumini = models.BooleanField(default = False)
    staff = models.BooleanField(default = False)
    something = models.BooleanField(default = False)
    yop = models.CharField(max_length = 63)
    degree = models.CharField(max_length = 63)
    dept = models.CharField(max_length = 63)
    specialization = models.CharField(max_length = 63)
    award =  models.CharField(max_length = 255)
    address = models.TextField(max_length = 355)
    submitted = models.BooleanField(default = False)
    ppo = models.CharField(max_length = 255, default = 'Alumni')


class Award_Form(models.Model):
    app_id = models.IntegerField()
    award = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["jpeg"])], null=True, blank=True)
    father_name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    yop = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    mob = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField(blank = True)
    ppo = models.CharField(max_length=255)
    distinctions = models.TextField(blank = True)
    distinctions_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    higher_eduction = models.TextField(blank=True)
    professional_exp = models.TextField(blank=True)
    prof_contri_papers = models.CharField(max_length=10)
    prof_contri_papers_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    prof_contri_patents = models.CharField(max_length=10)
    prof_contri_patents_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    prof_contri_membership = models.CharField(max_length=10)
    prof_contri_membership_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    prof_contri_books = models.CharField(max_length=10)
    prof_contri_books_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    prof_contri_others = models.CharField(max_length=10)
    prof_contri_others_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    prof_hon_award = models.TextField(blank=True)
    prof_hon_award_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    impact = models.TextField(blank=True)
    impact_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    nom_accom_con = models.TextField(blank=True)
    nom_accom_con_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    ls1_details = models.TextField(blank=True)
    ls1_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    ls2_details = models.TextField(blank=True)
    ls2_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    resume = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    additional_materials = models.TextField(blank=True)
    add_file = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)
    submitted = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "Nominations"

class ALAA_Form(models.Model):
    name_proposer = models.CharField(max_length = 200)
    details_proposer = models.TextField(blank = False)
    proposer_address = models.TextField(blank = False)
    proposer_mob = models.CharField(max_length = 16)
    proposer_email = models.CharField(max_length=63)
    name_nominee = models.CharField(max_length=63)
    nominee_father_name = models.CharField(max_length=63)
    dob = models.CharField(max_length=63)
    degree = models.CharField(max_length=63)
    dept = models.CharField(max_length=63)
    yop = models.CharField(max_length=63)
    rollno = models.CharField(max_length=63)
    otherquali = models.CharField(max_length=255)
    ppo = models.CharField(max_length=255)
    nominee_address = models.CharField(max_length=255)
    nominee_mob = models.CharField(max_length=16)
    nomionee_email = models.CharField(max_length=63)
    profile_pic = models.FileField(upload_to='documents/%Y/%m/%d')
    accom = models.FileField(upload_to='documents/%Y/%m/%d')



