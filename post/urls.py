from django.conf.urls import url
from django.urls import include , path
from . import views


app_name='Post'

urlpatterns = [
  path('' , views.post_list ),
  path('<int:id>', views.post_detail),

]