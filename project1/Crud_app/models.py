from django.db import models
from .Validators import validate_file_extension

# Create your models here.

class Management(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    emp_department = models.CharField(max_length=50)
    emp_salary = models.FloatField()
    emp_tasks = models.IntegerField()
    emp_manager = models.CharField(max_length=50)
    pan = models.FileField(upload_to ='uploads/' ,validators=[validate_file_extension])
    
    def __str__(self):
        return f'{self.emp_id}---{self.emp_name}'
    