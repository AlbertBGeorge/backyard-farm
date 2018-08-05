from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class check_crop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    temp_start = models.IntegerField()
    temp_end = models.IntegerField()
    pH_start = models.IntegerField()
    pH_end = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return self.name
