from django.urls import path
from .views import UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePAgeView, CreateProdilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePAgeView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProdilePageView.as_view(), name='create_profile_page'),

]
