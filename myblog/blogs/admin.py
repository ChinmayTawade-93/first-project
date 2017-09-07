from django.contrib import admin

# Register your models here.
from .models import blogger
from .models import BlogType
from .models import Bloggs
from .models import Comment

admin.site.register(blogger)
admin.site.register(BlogType)
admin.site.register(Bloggs)
admin.site.register(Comment)