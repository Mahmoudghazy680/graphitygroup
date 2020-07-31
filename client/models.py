from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils import timezone
# Create your models here.

class Client(models.Model):
    clientname       = models.CharField(max_length=150 , verbose_name=_("Client Name"), blank=True , null=True)
    clientlogo       = models.ImageField(upload_to='clientimg/', blank=True , null=True , verbose_name=_("Client Logo"))
    Desciption       = models.TextField( verbose_name=_("Desciption") , null=True , blank=True)
    clientlink       = models.URLField(blank=True , null=True , max_length=200 , verbose_name=_("Client Link"))
    clientactive     = models.BooleanField(default=True , verbose_name=_('Active'))


    def __str__(self):
      return self.clientname
    
    class Meta:
      ordering = ["clientname"]