from django.db import models



class Desk(models.Model):
    desk_name= models.CharField(max_length=50)
    is_available= models.BooleanField(default=False)
    date = models.DateField()
    employee_reserved_name = models.CharField(max_length=200) # the name of the employee who reserved the desk
    
    def __str__(self):
        return self.desk_name + ": " + self.employee_reserved_name



