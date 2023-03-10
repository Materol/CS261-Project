from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    #Register - user/create is full
    path('create/', CustomUserCreate.as_view(), name="creates_user"),
    #Logout - uses blacklist token from JWT
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]