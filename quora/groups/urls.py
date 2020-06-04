from django.urls import path
from . import views

urlpatterns=[
    path('', views.GroupeList.as_view(), name='list_groups'),
    path('create_group/', views.GroupeCreateView, name='create_group'),
    path('mygroups/', views.UserGroupe.as_view(), name='user_groups'),
    path('group/<int:id>/<str:action>/', views.join_or_leave, name='join_or_leave'),
    path('group/<int:id>/', views.GroupeDetail, name='groupe_detail'),
    path('group/<int:id>/members', views.GroupeMemberList, name='groupe_members'),
    path('group/<int:g_id>/members/remove/<int:id>/', views.RemoveMember,
        name='remove_member'),
    path('group/delete/<int:pk>/', views.DeleteGroupe.as_view(), name='delete_group' ),
    path('group/update/<int:pk>/', views.UpdateGroupe.as_view(), name='update_group' ),


]
