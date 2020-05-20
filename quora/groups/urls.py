from django.urls import path
from . import views

urlpatterns=[
    path('', views.GroupeList.as_view(), name='list_groups'),
    path('create_group/', views.GroupeCreateView.as_view(), name='create_group'),
    path('mygroups/', views.UserGroupe.as_view(), name='user_groups'),
    path('group/<int:id>/<str:action>/', views.join_or_leave, name='join_or_leave'),
    path('group/<int:id>/', views.GroupeDetail, name='groupe_detail'),
]
