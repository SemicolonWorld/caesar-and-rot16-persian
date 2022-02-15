from django.db import models
from django.utils import timezone

# Create your models here.


class EncryptAndDecryptModel(models.Model):
	CHOICES_ = (
		('c', 'caesar'),
		('r', 'rot16'),
	)
	CHOICES_ENC = (
		('e', 'encrypt'),
		('d', 'decrypt'),
	)
	text = models.TextField()
	result = models.TextField()
	what_type = models.CharField(max_length=1, choices=CHOICES_)
	encordec = models.CharField(max_length=1, choices=CHOICES_ENC)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.text}: {self.what_type}: {self.encordec}"