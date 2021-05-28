from django.db import models
import datetime
import re
# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['first_name']) < 2 :
            errors['first_name'] = "First Name needs to be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name needs to be at least 2 characters"
        if len(postData['password']) <8:
            errors['password'] = "The Passwords should be at least 8 char"
        if (postData['password']) !=(postData['confirm_password']):
            errors['last_name'] = "The Passwords doesn't match"
        if len(User.objects.filter(email=postData['email']))>0:
            errors['email'] = "This email already used"
        EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        if not EMAILREGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        return errors
class BookManager(models.Manager):
    def book_validator(self, postData):
        error = {}
        if len(postData['description'])<5:
            error['description']="Your description must be a little longer."
        return error
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email=models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __repr__(self):
        return f"User : {self.first_name} {self.last_name}"
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    user_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def book_add(book_title,book_description,book_by):
        bo=Book.objects.create(title=book_title,description=book_description,uploaded_by=book_by)
        bo.user_who_like(bo.id)
    def __repr__(self):
        return f"Book : {self.title} {self.description}"
    objects = BookManager()
