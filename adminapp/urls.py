from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Type', views.managetype, name='type'),
    path('Type-Edit', views.managetype_edit, name='type_edit'),
    path('Login', views.managelogin, name='login'),
    path('Logout', views.managelogout, name='logout'),
    path('Rate', views.managerate, name='rate'),
    path('rate_edit', views.managerate_edit, name='rate_edit'),
    path('feedback', views.managefeedback, name='feedback'),
    path('Slot', views.manageslot, name='slot'),
    path('Slot_edit', views.manageslot_edit, name='slot_edit'),
    path('User', views.manageuser, name='user'),
    path('Booking', views.managebooking, name='booking'),
    path('Booking-Report', views.managebookingreport, name='booking_report'),
    path('User-Report', views.manageuserreport, name='user_report'),
    path('Status-Report', views.managebookingstatusreport, name='status_report'),

]

