from django.db import models

STATUS = (  
    ('active','Active'),
    ('inactive','Inactive')
)

PUBLIC = (
    ('publish','Publish'),
    ('draft','Draft')
)

class Rooms(models.Model):
    name = models.CharField(max_length=150,blank=True, null=True)
    check_in_date = models.DateField()
    check_out_date =  models.DateField()
    number_of_guests = models.TextField(blank=True,null=True)
    room_number = models.TextField(blank=True,null=True)
    active = models.CharField(max_length=20, choices=STATUS, default='Inactive')
    created_date = models.DateTimeField(auto_now=True)
    update_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

