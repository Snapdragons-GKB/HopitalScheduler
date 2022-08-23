from django.db import models
import uuid
#from multiselectfield import MultiSelectField #pip3 install django-multiselectfield
#above not necessary, but will keep this here as a bookmark if we need it later



# Create your models here.

#Can we extend the basic signin formula, as in extending "useraccount" class?
#See https://stackoverflow.com/questions/16925129/generate-unique-id-in-django-from-a-model-field
#interesting that emailfield exists, nice
#Do we need to do anything to obfuscate password details? Feels like we do

insurance_tiers = [(0,"Person without Insurance"),(1,"Medicaid"),(2,"Medicare"),(3,"Private Insurer")]
ailment_categories = [('GP', "General Practice"), ('OS', "Orthopedic"), ('NS', "Neurosurgery"),('ER', "Emergency")]
treatment_status = [(0, "Awaiting response"), (1, "Scheduled for treatment"), (2, "Denied treatment"), (3, "Treatment completed")]

class Patient(models.Model):
    patientID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    username = models.CharField(min_length = 8)
    password = models.CharField(min_length = 8)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField(max=100)
    insurance_type = models.TextChoices(insurance_tiers) # unsure if I can have this in global state, might not work
    preexisting_conditions = models.TextField(max_length=80)
    current_medications = models.TextField(max_length=80)


class Scheduler(models.Model):
    schedulerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField() #interesting that this exists, nice
    username = models.CharField(min_length = 8) #note restriction here
    password = models.Password(min_length = 8)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Provider(models.Model):
    providerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField() #interesting that this exists, nice
    username = models.CharField(min_length = 8) #note restriction here
    password = models.Password(min_length = 8)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    personal_blurb = models.CharField(max_length=200) #lord knows they love to talk about themself
    provider_specialization = models.TextChoices(ailment_categories)
    insurances_taken = models.TextChoices(insurance_tiers)



#Now we have these three "person" classes, the below is the assembly line which they all have a part in (if full procedure scheduled)

class PatientRequest(models.Model):
    #maybe most important part, indicates what stage request is at
    request_status = models.TextChoices(treatment_status)

    #patient creates request, furnishes this data. After submission, request_status is awaiting response
    patientID = models.CharField() #we stamp this on every request
    ailment_category = models.TextChoices(ailment_categories)
    ailment_description = models.TextField(min_length = 20)
    preferred_date_range = models.Choices()
    
    #passes to scheduler, scheduler chooses schedule and doctor, can comment - request_status then either scheduled for treatment or denied treatment
    schedulerID = models.CharField() #filled in on either approval or denial, but not until then
    procedure_date = models.TextField()
    doctorID = models.CharField() #stamped on every scheduled approved procedure
    scheduling_comment = models.TextField() #if scheduler had denied and provides a reason (or accepted and wants to for some reason)
    #note, post-mvp can bounce back to patient for approval of surgeon

    #doctor's sole functionality is commenting on operation. Not sure if doctor should mark completed or if we just have it change automatically after "operation date"
    doctor_comment_on_operation = models.TextField()

#class TimePassing(models.Model):
    #currentDay = models.IntegerField(min=1, max=365)
