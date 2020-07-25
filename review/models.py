from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils import timezone
# Create your models here.
class Review(models.Model):
    
    revname      = models.CharField(max_length=150 , verbose_name=_("Client Name"), blank=True , null=True)
    revimg       = models.ImageField(upload_to='pstimg/', blank=True , null=True , verbose_name=_("Client Image"))
    revcontent   = models.TextField( verbose_name=_("Review Content") , null=True , blank=False)
    revlink      = models.URLField(blank=True , null=True , max_length=200 , verbose_name=_("Link"))
    revactive    = models.BooleanField(default=True)


    def __str__(self):
      return self.revname
    
    class Meta:
      ordering = ["revname"] 