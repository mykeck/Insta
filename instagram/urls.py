from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url(r'^$',views.index,name='index'),
    # url(r'^$',views.index,name='index'),
    url(r'^imagedetails/(\d+)',views.imagedetails,name ='imagedetails'),
    url(r'^new/image$',views.new_image,name='new-image'),
    url(r'^new/comment$',views.new_comment,name='new-comment'),

    url(r'^create/profile$',views.create_profile,name='create-profile'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^profiledetails/(\d+)',views.profiledetails,name ='profiledetails'),

    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    url(r'^search/', views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)