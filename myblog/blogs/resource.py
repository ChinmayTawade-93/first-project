from tastypie.resources import ModelResource
from .models import *
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields	
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = "user"
		authorization = Authorization()
		always_return_data = True
		filtering = {'username': ALL_WITH_RELATIONS}

class BlogTypeResource(ModelResource):
	class Meta:
		queryset = BlogType.objects.all()
		resource_name = "blog_type"
		always_return_data = True

class bloggerResource(ModelResource):
	class Meta:
		queryset = blogger.objects.all()
		resource_name = "blogger"
		always_return_data = True		

class BloggsResource(ModelResource):
	blogger = fields.ForeignKey('blogs.resource.bloggerResource', 'blogger')
	blog_type = fields.ForeignKey(BlogTypeResource, 'blog_type')
	class Meta:
		queryset = Bloggs.objects.all()
		resource_name = "bloggs"
		always_return_data = True

class CommentResource(ModelResource):
	bloggs = fields.ForeignKey(BloggsResource, 'bloggs')
	owner = fields.ForeignKey(bloggerResource, 'owner')
	class Meta:
		queryset = Comment.objects.all()
		resource_name = "comment"
		always_return_data = True
			
  

