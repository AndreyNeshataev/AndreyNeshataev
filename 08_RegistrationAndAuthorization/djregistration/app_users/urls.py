from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser, MyUser  # login_view,


urlpatterns = [
    # path('login/', login_view, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('account/', MyUser.as_view(), name='account'),
]
