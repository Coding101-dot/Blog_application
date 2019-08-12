"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from Blog_application.blogz import views

app_name = 'blogz'

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post_share/(?P<post_id>\d+)/$', views.post_share, name='post_share'),
    url(r'comment/(?P<post_id>\d+)/$', views.comment, name='comment'),
    url(r'post/$', views.add_post, name='add_post'),


]
