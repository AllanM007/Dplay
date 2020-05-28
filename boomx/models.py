from django.db import models
from PIL import Image

class Track(models.Model):
	name = models.CharField(max_length=50)
	audio = models.FileField(upload_to='audio')
	genre = models. CharField(max_length=15)
	image = models.ImageField(default='default.jpg', upload_to='album_art')
	created_on = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
		