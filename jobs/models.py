from django.db import models

# Create your models here.

class Job(models.Model):

# this image vairble allows us to set the image in the post and it uploads it to the images file
    image = models.ImageField(upload_to='images/')
    
    """
    this code allows us to set the summary of the post, charField makes a textbox more or less and we are allowing the max lenght to be 200 characters.
    """
    summary = models.CharField(max_length=200)

# this funtion returns the summary of each post, in the admin panel, so when opened it shows waht each post is instead of the default of object 1, 2, 3, 4, so on.
    def __str__(self):
        return self.summary
