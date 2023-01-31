from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    docs_name=models.CharField(max_length=255)
    docs_spec=models.CharField(max_length=255)
    dept_name=models.ForeignKey(Departments, on_delete=models.CASCADE)    
    docs_image=models.ImageField(upload_to='doctors')

    
    def __str__(self):
        return 'Dr ' + self.docs_name + ' - (' + self.docs_spec + ')'

class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    docs_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
