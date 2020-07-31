from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Service(models.Model):
    servname     = models.CharField(default='Service_name', max_length=50, blank=False , null=False,verbose_name=_('Service Name')) 
    mainserv     = models.ForeignKey('self' , limit_choices_to={'mainserv__isnull' : True} , on_delete=models.CASCADE , blank=True , null=True , verbose_name=_('Main Service'))
    servimg      = models.ImageField(upload_to='servimg/', blank=True , null=True , verbose_name=_('Service Image'))
    servdesc     = models.TextField(blank=True , null=True, verbose_name=_('Service Decsription'))
    servactive   = models.BooleanField(default=True , verbose_name=_('Active'))



    def __str__(self):
        return self.servname