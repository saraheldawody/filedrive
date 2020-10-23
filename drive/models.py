from django.db import models
from django.core.validators import FileExtensionValidator
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.User.id, filename)
# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    CreatedOn = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    File = models.FileField(upload_to=user_directory_path)
    UploadedOn = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    @property
    def extension(self):
        if self.File.url.endswith('pdf'):
            return 'PDF'
        else:
            return 'pptx'
    

class LookupWords(models.Model):
    Word = models.CharField(max_length=100)
    Frequency = models.IntegerField()
    File = models.ForeignKey(File,on_delete=models.CASCADE)
    @property
    def user(self):
        return self.File.User