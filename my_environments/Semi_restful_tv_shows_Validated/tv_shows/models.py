from django.db import models
# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = 'Network needs to be at least 3 characters'
        if len(postData['description'])>0 :
            if len(postData['description'])<10:
                errors['description'] = "Description needs to be at least 10 characters"
        return errors
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=100)
    release_date=models.DateField()
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()
    def __repr__(self):
        return f"Show : {self.title} {self.desc}"
    def update_show(self,a,b,c,d):
        self.title=a
        self.network=b
        self.release_date=c
        self.desc=d
        self.save()
    def delete_show(self,a):
        self.id=a
        self.delete()
        
