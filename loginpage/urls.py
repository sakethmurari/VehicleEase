from django.urls import path
from .views import login,welcome,logout,book_vehicle,history,profile,history_remove,history_update,update_profile
urlpatterns = [
    path('',login,name='login'),
    path('welcome/',welcome,name='welcome'),
    path('logout/',logout,name='logout'),
    path('book_vehicle/',book_vehicle,name='book_vehicle'),
    path('history/',history,name='history'),
    path('profile/',profile,name='profile'),
    path('history/update/<int:id>/', history_update, name='history_update'),
    path('history/delete/<int:id>/', history_remove, name='history_remove'),
    path('update_profile/<int:id>/', update_profile,name='update_profile'),
]