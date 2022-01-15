from django.db import models

STATUS = (  
    ('active','Active'),
    ('inactive','Inactive')
)

PUBLIC = (
    ('publish','Publish'),
    ('draft','Draft')
)
class Service(models.Model):
    name = models.CharField(max_length=150,blank=True, null=True)
    active = models.CharField(max_length=20, choices=STATUS, default='Inactive')
    created_date = models.DateTimeField(auto_now=True)
    update_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    name = models.CharField(max_length=150,blank=True, null=True)
    check_in_date = models.DateField()
    check_out_date =  models.DateField()
    number_of_guests = models.TextField(blank=True,null=True)
    room_number = models.TextField(blank=True,null=True)
    services = models.ManyToManyField(Service,blank=True, null=True)
    price = models.CharField(max_length=150,blank=True, null=True)
    thumbnail = models.ImageField(upload_to="rooms_thumbnail", blank=True, null=True)
    active = models.CharField(max_length=20, choices=STATUS, default='Inactive')
    created_date = models.DateTimeField(auto_now=True)
    update_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def all_services(self):
        return ",".join([str(p) for p in self.services.all()])
    

