from django.urls import path,include
from User import views
app_name='User'


urlpatterns = [
     path('myprofile/',views.myprofile,name="myprofile"),
     path('homepage/',views.homepage,name="homepage"),
     path('editprofile/',views.editprofile,name="editprofile"),
     path('changepassword/',views.changepassword,name="changepassword"),
     path('request/',views.request,name="request"),
     path('myrequest/',views.myrequest,name="myrequest"),
     path('predict/',views.predict_video,name="predict"),
]