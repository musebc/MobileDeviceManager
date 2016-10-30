from django.db import models
from device.models import DeviceModel

# Create your models here.

def app_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.name, instance.version)

class Application(models.Model):
	"""docstring for Application"""
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	operatingSystem = models.CharField(max_length=40,default='Android')
	version = models.CharField(max_length=40)
	partNumber = models.CharField(max_length=15)
	pricePerMonth = models.FloatField()
	description = models.TextField()
	recent_updates = models.TextField(null=True)
	icon = models.ImageField(upload_to=app_directory_path)
	banner = models.ImageField(upload_to=app_directory_path)
	applicationFile = models.FileField(upload_to=app_directory_path)
	created = models.DateTimeField(auto_now_add=True)
	number_of_downloads = models.PositiveIntegerField(default=0)
	valid_device_models = models.ManyToManyField(
		DeviceModel,
		through='AppModelList',
		through_fields=('app', 'device_model'),
		)


	def __str__(self):
		return self.name

class Screenshot(models.Model):
	"""docstring for Screenshot"""
	
	application = models.ForeignKey(Application)
	image = models.ImageField(upload_to=app_directory_path)

	def __str__():
		return self.name

class Video(models.Model):
	application = models.ForeignKey(Application)
	video = models.FileField(upload_to=app_directory_path)	

class Review(models.Model):
	title = models.CharField(max_length=25)
	body = models.TextField(max_length=1000)
	rating = models.PositiveIntegerField(null=True)
	app = models.ForeignKey(Application)

	def __str__():
		return self.title

class AppModelList(models.Model):
	app = models.ForeignKey(Application)
	device_model = models.ForeignKey(DeviceModel)