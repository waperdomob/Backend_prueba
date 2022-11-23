from django.urls import path

from apps.users.views import login, logout

urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
]