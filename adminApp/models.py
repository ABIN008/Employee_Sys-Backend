from django.db import models

# Create your models here.
# Blood_Groups = (
#     ("A+", "A+"),
#     ("A-", "A-"),
#     ("B+", "B+"),
#     ("B-", "B-"),
#     ("O+", "O+"),
#     ("O-", "O-"),
#     ("AB+","AB+"),
#     ("AB-", "AB-"),
# )
# Marital_Statuses = (
#     ("SINGLE", "SINGLE"),
#     ("MARRIED", "MARRIED"),
#     ("DIVORCED", "DIVORCED")
# )    
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_Number = models.IntegerField()
    emergency_Contact_Number = models.IntegerField()
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    dob = models.DateField()
    martial_Status = models.CharField(max_length=100)
    Blood_Group = models.CharField(max_length=100)
    # marital_status = models.CharField(max_length = 20, choices = Marital_Statuses, default = '')
    # Blood_Group = models.CharField(max_length = 20, choices = Blood_Groups, default = '')
    job_Title = models.CharField(max_length=100)
    work_Location = models.CharField(max_length=100)
    date_Of_Joining = models.DateField()
    reporting_To = models.CharField(max_length=100)
    linkedin_Link =  models.URLField(max_length=300)
    Photo_File_Name = models.CharField(max_length=100)