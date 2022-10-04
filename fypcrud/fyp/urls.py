from django.contrib import admin
from django.urls import path
from fyp import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path("", views.Welcome, name='Welcome'),

    path("Register", views.Register, name='Register'),
    path("Login",auth_view.LoginView.as_view(template_name='login.html'),name='Login'),
    path("Logout",auth_view.LogoutView.as_view(template_name='logout.html'),name='Logout'),
    path("Dashboard",views.index,name='index'),
    path("Profile",views.profile,name='profile'),


    path("GuestRegistration", views.GuestRegistration, name='GuestRegistration'),
    path("ResidentRegistration", views.ResidentRegistration, name='ResidentRegistration'),


    path("ViewDetailsResident", views.ViewDetailsResident, name='ViewDetailsResident'),
    path("ViewDetailsGuest", views.ViewDetailsGuest, name='ViewDetailsGuest'),

    path("barcode", views.barcode, name='barcode'),
    path("issuecard/<int:id>/<str:type>",views.issuecard,name='issuecard'),

     path("ViewDetailsGuest/history/<int:id>/", views.historys, name='history'),

    path("ViewDetailsResident/delete/<int:id>/", views.delete_resident, name='delete_resident'),
    path("ViewDetailsGuest/delete/<int:id>/", views.delete_Guest, name='delete_guest'),

    path("Approvalpage/reject/<int:id>/", views.delete_tempresident, name='delete_tempresident'),
    path("Approvalpage/approve/<int:id>/", views.approve_tempresident, name='approve_tempresident'),


    path("ViewDetailsResident/<int:id>/", views.Edit_Resident, name='Edit_Resident'),
    path("ViewDetailsResident/resident/<int:id>/", views.Residentupdate, name='Residentupdate'),
    path("ViewDetailsGuest/<int:id>/", views.Edit_Guest, name='Edit_Guest'),
    path("ViewDetailsGuest/guest/<int:id>/", views.Guestupdate, name='Guestupdate'),
    
    path("Approvalpage",views.approvalpage,name='approvalpage'),
    
    #password reset:>>
   path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),



]