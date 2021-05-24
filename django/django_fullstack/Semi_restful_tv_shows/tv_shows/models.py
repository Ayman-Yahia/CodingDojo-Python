from django.db import models

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=100)
    release_date=models.DateField()
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
        
