from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('',views.index0,name='index0'),
    path('index0',views.index0, name='index0'),
    path('gra_res',views.gra_res, name='gra_res'),
    path('pg_res',views.pg_res, name='pg_res'),
    path('res_form0',views.res_form0, name='res_form0'),
    path('res_form1',views.res_form1, name='res_form1'),
    path('pg_res_form0',views.pg_res_form0, name='pg_res_form0'),
    path('pg_res_form1',views.pg_res_form1, name='pg_res_form1'),
    path('resume0',views.resume0, name='resume0'),
    path('resume1',views.resume1, name='resume1'),
    path('pg_resume0',views.pg_resume0, name='pg_resume0'),
    path('pg_resume1',views.pg_resume1, name='pg_resume1'),

]