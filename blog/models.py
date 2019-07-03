from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # auto_now_add=True - This assigns the current date and time to this field whenever an instance of this class is created.
    last_modified = models.DateTimeField(auto_now=True) # auto_now=True. This assigns the current date and time to this field whenever an instance of this class is saved
    categories = models.ManyToManyField('Category', related_name='posts') # By adding a related_name of posts, we can access category.posts to give us a list of posts with that category.

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # If a post is deleted, then we don’t want the comments related to it hanging around.
