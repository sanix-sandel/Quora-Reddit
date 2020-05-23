from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('profile/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
]
