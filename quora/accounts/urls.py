from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('myprofile/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:id>/', views.See_Profile, name='see_profile'),
]
