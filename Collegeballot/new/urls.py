from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("login.html", views.login, name='login'),
    path('profile.html',views.profile,name='profile'),
    path('p_cr_reg.html', views.p_cr_reg, name="p_cr_reg"),
    path('p_depthead.html', views.p_depthead, name="p_depthead"),
    path('p_president_interview.html', views.p_president_interview, name="p_president_interview"),
    path('p_vote_cr.html', views.p_vote_cr, name="p_vote_cr"),
    path('p_final_president.html', views.p_final_president, name="p_final_president"),
    path('pcr_votecount',views.pcr_votecount,name="pcr_votecount"),
    path('p_poll.html',views.p_poll,name="p_poll"),
    path('p_final',views.p_final,name="p_final"),
    path('results.html',views.results,name="results"),
    path("hod_login.html", views.hod_login, name='hod_login'),
    path("display.html", views.display, name='display'),
    path("hod_trial.html", views.hod_trial, name='hod_trial'),
    path("dn",views.dn,name='dn'),
    path("knowtheprocess.html",views.knowtheprocess,name='knowtheprocess')

]