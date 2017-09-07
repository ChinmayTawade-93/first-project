from django.db import models
from django.contrib.auth.models import User
from django_fsm import FSMField, transition
# Create your models here.
class blogger(models.Model):
	user = models.OneToOneField(User, related_name='blogger')
	name = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email_id = models.CharField(max_length=200)
	isd = models.CharField(max_length=3)
	number = models.CharField(max_length=12)
	def __str__(self):
		return self.name
 
class BlogType(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title

class Bloggs(models.Model):
	blogger = models.ForeignKey(blogger, related_name="bloggs")
	blog_type = models.ForeignKey(BlogType,related_name="bloggs")
	title = models.CharField(max_length=200)
	is_public = models.BooleanField(default=False)
	description = models.CharField(max_length=1000)
	state = FSMField(default='new')

	def __str__(self):
		return self.title

	@transition(field=state, source=["new","draft"], target="draft")
	def draft(self):
		pass
	@transition(field=state, source=["new","draft"], target="publish")
	def draft(self):
		pass

	@transition(field=state, source=["publish"], target="cancel")
	def draft(self):
		pass

