from django.db import models

# Create your models here.
class Home (models.Model):
    home_hello = models.CharField(max_length=200)
    home_lorem = models.TextField()
    home_video = models.FileField(upload_to="video")
    def __str__(self):
        return f"{self.home_hello} | {self.home_lorem} | {self.home_video}"

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = 'Home'

class AboutUs(models.Model):
    about_lorem = models.TextField()
    about_name = models.CharField(max_length=2000)
    about_manzil = models.CharField(max_length=2000)
    about_call = models.IntegerField()
    about_email = models.CharField(max_length=2000)
    about_video = models.FileField(upload_to="video")
    about_clent = models.IntegerField()
    about_projects = models.IntegerField()
    about_practice = models.IntegerField()

    def __str__(self):
        return f"{self.about_lorem} | {self.about_name} | {self.about_manzil} | {self.about_call} | {self.about_email} | {self.about_video} |" \
               f"  | {self.about_clent} | {self.about_projects} | {self.about_practice}"

    class Meta:
        verbose_name = "AboutUs"
        verbose_name_plural = "AboutUs"

class Carusel(models.Model):
    img = models.ImageField(upload_to="img")

    def __str__(self):
        return f"{self.img}"

    class Meta:
        verbose_name = "Carusel"
        verbose_name_plural = "Carusel"



class Contact(models.Model):
    manzil = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    call = models.IntegerField()

    def __str__(self):
        return f"{self.manzil} | {self.email} | {self.call}"

    class Meta:
        verbose_name = "Cantact"
        verbose_name_plural = "Contact"



class Icon(models.Model):
    icon = models.ImageField(upload_to="jpg")
    def __str__(self):
        return f"{self.icon}"
    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icon"
