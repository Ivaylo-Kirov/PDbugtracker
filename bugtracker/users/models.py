from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self): #override the parent save method in order to resize the image
        # super().save(*args, **kwargs) #don't lose the actual save functionality - added args and kwargs as Corey said this was needed prior to live deployment
        super().save() # removed them for now or login wasn't working on Staging
        img = Image.open(self.image.path) #create an image instance. Image is the Pillow class. "self.image.path" refers to the Profile field image from the model definition

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)