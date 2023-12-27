from django.db import models
import uuid


# Create your models here.
class Client(models.Model):
  # Autocreated UUID
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  # zip code, city, street in separte field
  zip = models.IntegerField()
  city = models.CharField(max_length=30)
  address = models.CharField(max_length=50)
  
  def __str__(self):
        return self.name
  