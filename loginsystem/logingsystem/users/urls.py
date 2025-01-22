from django.urls import path
from .import views

#url patterns
urlpatterns = [

    #sign up eke pattern eka
    path ('signup/',views.signup_view,name='signup'),

    #signin eke pattern eka
    path ('signin/',views.signin_view, name='signin'),

    #logout eke pattern eka
    path ('logout/',views.logout_view, name='logout'),

    #home eke pattern eka
    path('normal-user/', views.normal_user_home, name='normal_user_home'),

    #hotel admin dashboard eke pattern eka
    path('hotel-admin',views.hotel_admin_dashboard, name='hotel_admin_dashboard'),

    #main user ge pattern eka
    path('main-admin', views.main_admin_dashboard, name='main_admin_dashboard'),

    #server eka run weddi apat yann ona, thene path eka
    path('', views.signup_view, name='home'),
]