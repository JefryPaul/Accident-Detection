from django.urls import path,include
from Guest import views 
app_name='Guest'

urlpatterns = [
        path('login/',views.login,name="login"),
        path('userregistration/',views.userregistration,name="userregistration"),
        path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
        path('index/',views.index,name='index'),

]