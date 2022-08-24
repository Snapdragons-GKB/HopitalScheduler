from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    class insurance(models.TextChoices):
        NONE = 0, 'Without Insurance'
        MEDICAID = 1, 'Medicaid'
        MEDICARE = 2, 'Medicare'
        PRIVATE = 3, 'Private'

    
    patientID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patientpersonal')
    patient_age = models.IntegerField()
    patient_insurance_type = models.CharField(max_length=20, choices=insurance.choices, default=insurance.NONE)
    patient_preexisting_conditions = models.TextField(max_length=80)
    patient_current_medications = models.TextField(max_length=80)

class Scheduler(models.Model):
    schedulerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedulerpersonal')

class Provider(models.Model):
    class insurance(models.TextChoices):
        NONE = 0, 'Without Insurance'
        MEDICAID = 1, 'Medicaid'
        MEDICARE = 2, 'Medicare'
        PRIVATE = 3, 'Private'

    class specialty(models.TextChoices):
        NONE = 0, 'None'
        CARDIOLOGY = 1, 'Cardiology'
        NEUROLOGY = 2, 'Neurology'
        PEDIATRICS = 3, 'Pediatrics'
        SURGERY = 4, 'Surgery'
        DENTAL = 5, 'Dental'
        GENERAL_MEDICINE = 6, 'General Medicine'
        PSYCHIATRY = 7, 'Psychiatry'
        RADIOLOGY = 8, 'Radiology'
        SURGICAL = 9, 'Surgical'
        OTHER = 10, 'Other'

    providerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='providerpersonal')
    personal_blurb = models.CharField(max_length=200)
    provider_specialization = models.CharField(max_length=20, choices=specialty.choices, default=specialty.NONE)
    insurances_taken = models.CharField(max_length=20, choices=insurance.choices, default=insurance.NONE)


class PatientRequest(models.Model):
    class request_status(models.TextChoices):
        PENDING = 0, 'Awating Response'
        ACCEPTED = 1, 'Accepted'
        REJECTED = 2, 'Rejected'
        CANCELLED = 3, 'Cancelled'
        COMPLETED = 4, 'Completed'
    
    class ailment_category(models.TextChoices):
        NONE = 0, 'None'
        CARDIOLOGY = 1, 'Cardiology'
        NEUROLOGY = 2, 'Neurology'
        PEDIATRICS = 3, 'Pediatrics'
        SURGERY = 4, 'Surgery'
        DENTAL = 5, 'Dental'
        GENERAL_MEDICINE = 6, 'General Medicine'
        PSYCHIATRY = 7, 'Psychiatry'
        RADIOLOGY = 8, 'Radiology'
        SURGICAL = 9, 'Surgical'
        OTHER = 10, 'Other'


    request_status = models.CharField(max_length=20, choices=request_status.choices, default=request_status.PENDING)
    patientID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    ailment_category = models.CharField(max_length=20, choices=ailment_category.choices, default=ailment_category.NONE)
    ailment_description = models.CharField(max_length=80)
    preferred_date_range = models.DateField()
    schedulerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduler')
    procedure_date = models.DateField()
    doctorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    scheduling_comment = models.TextField()
    doctor_comment_on_operation = models.TextField()

