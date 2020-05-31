from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('notifications/', views.notifications, name='notifications'),
    path('myprofile/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:id>/', views.See_Profile, name='see_profile'),
    path('profile/<int:id>/follow/', views.follow, name='follow'),
    path('notifs/', views.personal_notifications, name='personal_notifs'),

]
