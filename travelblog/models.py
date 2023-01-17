from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Tipuri(models.Model):
    nume = models.CharField(max_length=5000)

    def __str__(self):
        return self.nume

    def get_absolute_url(self):
        # return reverse('articole_details', args=(str(self.id)))
        return reverse('home')

class Postare(models.Model):
    titlu = models.CharField(max_length=500)
    imagine_blog = models.ImageField(null=True, blank=True, upload_to="imagini/")
    titlu_nav = models.CharField(max_length=500)
    # return reverse('articole_details',)
    cuprins = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_postare =models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='postare_blog')
    tipuri = models.CharField(max_length=250, default='calatorii')

    def __str__(self):        # return f"Postare(titlu={self.titlu}, cuprins={self.cuprins}, autor={self.autor})"
        return self.titlu + ' | ' + str(self.autor)

    def get_absolute_url(self):
        # return reverse('articole_details', args=(str(self.id)))
        return reverse('home')