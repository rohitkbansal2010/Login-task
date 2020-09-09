from django.urls import path
from .views import SignUpView, userList, deleteUser

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', userList, name='userList'),
    path('<int:user_id>/', deleteUser, name='deleteUser'),
]
