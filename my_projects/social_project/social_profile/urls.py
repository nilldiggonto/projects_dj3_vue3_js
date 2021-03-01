from django.urls import path
from .views import socialprofileView,follow_userView,unfollow_userView,followerView,followView,edit_avatarView

urlpatterns = [
    path('avatar/',edit_avatarView,name='social-edit-avatar'),
    path('<str:username>',socialprofileView,name='social-profile'),
    path('<str:username>/follow/',follow_userView,name='social-user-profile-follow'),
    path('<str:username>/unfollow/',unfollow_userView,name='social-user-profile-unfollow'),
    path('<str:username>/follower/list/',followerView,name='social-follower-list'),
    path('<str:username>/follows/list/',followView,name='social-follow-list'),


]