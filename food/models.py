from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Items(models.Model):

  def __str__(self):
    return self.item_name

  user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
  id = models.AutoField(primary_key=True)
  item_name = models.CharField(max_length=255)
  item_description = models.TextField(blank=True)
  item_price = models.IntegerField()
  item_image = models.CharField(max_length=500, default='food/food-placeholder.jpg')

  def get_absolute_url(self):
    return reverse('food:detail', kwargs={"pk": self.pk})