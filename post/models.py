from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils import timezone
#from category import Service
#from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    posttitle   = models.CharField(max_length=150 , verbose_name=_("Title"), blank=True , null=True)
    mainimg     = models.ImageField(upload_to='pstimg/', blank=True , null=True , verbose_name=_("Header Image"))
    #pstcat     = models.ForeignKey('Service' , on_delete=models.CASCADE , blank=True , null=True , verbose_name=_("Service"))
  # postserv    = models.ForeignKey('Service' , limit_choices_to={'postserv__isnull' : True} , on_delete=models.CASCADE , blank=True , null=True , verbose_name=_('Main Service'))
    postimg     = models.ImageField(upload_to='pstimg/', blank=True , null=True , verbose_name=_("Post Image"))
    content     = models.TextField( verbose_name=_("Post Content") , null=True , blank=False)
    link        = models.URLField(blank=True , null=True , max_length=200 , verbose_name=_("Post Link"))
    created_at  = models.DateTimeField(auto_now_add=True, )
  # updated_at  = models.DateTimeField(auto_now_add=True, default=timezone.now)
    postactive  = models.BooleanField(default=True , verbose_name=_('Active'))
    tags        = models.CharField(blank=True, max_length=100)
    slug        = models.SlugField(null=True , blank=True)



    def __str__(self):
      return self.posttitle
    
    class Meta:
      ordering = ["-created_at", "posttitle"]