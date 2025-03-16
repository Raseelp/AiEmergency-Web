from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('', views.login),
    path('login_post', views.login_post),
    path('admin_add_ambulance', views.admin_add_ambulance),
    path('admin_add_hospital',views.admin_add_hospital),
    path('admin_add_hospital_post',views.admin_add_hospital_post),
    path('admin_admin_home',views.admin_admin_home),
    path('admin_feedback',views.admin_feedback),
    path('admin_notification',views.admin_notification),
    path('admin_view_ambulance',views.admin_view_ambulance),
    path('admin_hospital',views.admin_hospital),
    path('admin_search_hospital',views.admin_search_hospital),
    path('admin_search_ambulance', views.admin_search_ambulance),
    path('delete_hospital/<int:id>',views.delete_hospital),
    path('delete_ambulance/<int:id>', views.delete_ambulance),
    path('edit_hospital/<id>',views.edit_hospital),
    path('edithospitalPost', views.edithospitalPost),
    path('edit_ambulance/<id>',views.edit_ambulance),
    path('editAmbulancePost', views.editAmbulancePost),
    path('admin_notification_post', views.admin_notification_post),


    path('hospital_add_ambulance_hospital',views.hospital_add_ambulance_hospital),
    path('hospital_ambulance_message',views.hospital_ambulance_message),
    path('hospital_ambulance_registration',views.hospital_ambulance_registration),
    path('hospital_hospital_home',views.hospital_hospital_home),
    path('hospital_view_message',views.hospital_view_message),
    path('hospital_patient_condition',views.hospital_patient_condition),
    path('hospital_add_ambulance_post',views.hospital_add_ambulance_post),
    path('hospital_view_message',views.hospital_view_message),
    path('hospital_ambulance_message_post', views.hospital_ambulance_message_post),
    path('trackAmbulance/<id>',views.trackAmbulance),
    path('delete_patient_info/<int:id>',views.delete_patient_info),
    path('hospital_view_ambulance', views.hospital_view_ambulance),
    path('editAmbulancePost_hospital', views.editAmbulancePost_hospital),
    path('hospital_search_ambulance', views.hospital_search_ambulance),
    path('hospital_track_ambulances/<id>', views.hospital_track_ambulances),
    path('edit_ambulance_hospital/<id>', views.edit_ambulance_hospital),
    path('delete_ambulance_hospital/<int:id>', views.delete_ambulance_hospital),

    path('logincode', views.logincode),
    path('view_nearest_ambulances', views.view_nearest_ambulances),
    path('view_nearest_ambulances2', views.view_nearest_ambulances2),
    path('sendfeedback', views.sendfeedback),
    path('view_nearest_traffic_notifivcation', views.view_nearest_traffic_notifivcation),
    path('user_send_ambulance_request', views.user_send_ambulance_request),
    path('view_messages_from_hospital', views.view_messages_from_hospital),
    path('send_patient_info', views.send_patient_info),
    path('user_registration', views.user_registration),
    path('updatelocation', views.updatelocation),
    path('update_status/', views.update_ambulance_status),
    path('get_ambulance_requests/', views.get_ambulance_requests,),
    path('accept_request/<int:request_id>/', views.ambulance_accept_request),
    path('complete_request/<int:request_id>/', views.ambulance_complete_request,),
    path('get-username/<int:lid>/', views.get_username),
    path('delete_ambulance_request', views.delete_ambulance_request),
    path('upload_voice_message/',views.upload_voice_message),



]
