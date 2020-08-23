from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #includes username, email and password
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    bio = models.CharField(max_length=300, default = "Hey there! I'm handeling my accounts")
    contactNo = models.CharField(max_length=14,default = "1234567890")
    firstN = models.CharField(max_length=20, default = "Sita")
    lastN = models.CharField(max_length=20, default = "Ram")
    linkedIn = models.URLField(max_length=100, default = "http://linkedin.com")
    github = models.URLField(max_length=50, default = "http://github.com")
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        if img.height > 100 or img.width > 100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def get_absolute_url(self):
       return reverse('profile',kwargs = {'pk': self.user.pk})
