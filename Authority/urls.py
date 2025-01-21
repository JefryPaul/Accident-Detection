from django.urls import path,include
from Authority import views
app_name='Authority'


urlpatterns = [
        path('homepage/',views.homepage,name="homepage"),
        path('myprofile/',views.myprofile,name="myprofile"),
        path('editprofile/',views.editprofile,name="editprofile"),
        path('changepassword/',views.changepassword,name="changepassword"),
        path('viewrequest/',views.viewrequest,name="viewrequest"),


]