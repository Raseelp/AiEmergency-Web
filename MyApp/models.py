from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class hospital_table(models.Model):
    LOGIN= models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image=models.FileField()
    place = models.CharField(max_length=100)
    pin=models.IntegerField()
    post = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contactNumberOne=models.BigIntegerField()
    contactNumberTwo=models.BigIntegerField()
    Latitude=models.FloatField()
    Longitude=models.FloatField()

class ambulance_table(models.Model):
    LOGIN= models.ForeignKey(login_table,on_delete=models.CASCADE)
    VehicleNumber = models.CharField(max_length=100)
    Hospital= models.ForeignKey(hospital_table,on_delete=models.CASCADE)
    Type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)

class location_table(models.Model):
    LOGIN= models.ForeignKey(login_table,on_delete=models.CASCADE)
    # Latitude = models.FloatField()
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    date=models.CharField(max_length=100)


class user_table(models.Model):
    LOGIN= models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    PhoneNumber=models.BigIntegerField()
    email = models.CharField(max_length=100)


class feedback_table(models.Model):
    Feedback=models.CharField(max_length=100)
    USER_ID= models.ForeignKey(user_table,on_delete=models.CASCADE)
    date=models.DateTimeField()

class message_table(models.Model):
    EmergencyMessage=models.CharField(max_length=100)
    AMBULANCE= models.ForeignKey(ambulance_table,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()

class user_message_table(models.Model):
    EmergencyMessage=models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.TimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

class patient_table(models.Model):
    AMBULANCE_ID= models.ForeignKey(ambulance_table,on_delete=models.CASCADE)
    PatientCondition = models.CharField(max_length=100)
    date=models.DateTimeField


class notification_table(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateTimeField()

class ambulance_request_table(models.Model):
    AMBULANCE_ID = models.ForeignKey(ambulance_table, on_delete=models.CASCADE, null=True, blank=True)
    USER_ID= models.ForeignKey(user_table,on_delete=models.CASCADE)
    username=models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=100)
    date=models.DateTimeField()
    request=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
































