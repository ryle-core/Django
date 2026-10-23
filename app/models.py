from django.db import models

# Create your models here.

class Register(models.Model):
    fullname = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[

            ('male', 'male'),
            ('female', 'female'),
            ('other', 'other'),
        ]

    )
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    year = models.IntegerField(
     choices=[
         (1, 'year 1'),
         (2, 'year 2'),
         (3, 'year 3'),
         (4, 'year 4'),

         
         
         

              
         ]

    )
    def __str__(self):
     return self.name 


      

