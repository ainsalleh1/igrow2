from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from django.conf.urls import url
# from .import index

# from .api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('templates\MainGroup.html',views.mainGroup, name="MainGroup"),
    path('templates\group.html',views.group, name="Group"),
    path('templates\MyGroup.html',views.myGroup, name="MyGroup"),
 

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







