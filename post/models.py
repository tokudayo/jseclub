from django.db import models
from django.contrib.auth.models import User
from comment.models import Comment

# Create your models here.
class Post(models.Model):
	comments = models.ManyToManyField(Comment)
	type = models.CharField(max_length = 16)
	title = models.CharField(max_length = 45)
	body = models.TextField()
	pub_date = models.DateTimeField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	def __str__ (self):
		return self.title

# Create your models here.
