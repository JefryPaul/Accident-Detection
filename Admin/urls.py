from django.urls import path,include
from Admin import views
app_name='Admin'


urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('district/',views.district,name="district"),
    path('category/',views.category,name="category"),
    path('place/',views.place,name="place"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('deletedis/<int:did>',views.deletedis,name="deletedis"),
    path('deletediss/<int:didd>',views.deletediss,name="deletediss"),  #category
    path('editdis/<int:eid>',views.editdis,name="editdis"), #district
    path('admin/',views.admin,name="admin"),
    path('deletedisss/<int:diddd>',views.deletedisss,name="deletedisss"),  #admin
    path('deletedplace/<int:diplace>',views.deletedplace,name="deletedplace"),  #place
    path('deletedsubcategory/<int:disubcategory>',views.deletedsubcategory,name="deletedsubcategory"),  #subplace
    path('editplace/<int:eid>',views.editplace,name="editplace"),#place
    path('editsubcategory/<int:eid>',views.editsubcategory,name="editsubcategory"),#place
    path('viewusers/',views.viewusers,name="viewusers"),
    path('deletedusers/<int:did>',views.deletedusers,name="deletedusers"),
    path('authorityreg/',views.authorityreg,name="authorityreg"),
    path('hospitalreg/',views.hospitalreg,name="hospitalreg"),
    path('viewauthority/',views.viewauthority,name="viewauthority"),
    path('accept/<int:aid>',views.accept,name="accept"), 
    path('reject/<int:rid>',views.reject,name="reject"), 
    path('viewhospital/',views.viewhospital,name="viewhospital"),
    path('haccept/<int:haid>',views.haccept,name="haccept"), 
    path('hreject/<int:hrid>',views.hreject,name="hreject"), 


]