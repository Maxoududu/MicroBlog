from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=60)
	description = models.TextField()
	created = model.DateTimeField(auto_now_add=true)

	def _unicode_(self):
		returnself.title

### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)

