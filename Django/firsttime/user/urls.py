from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.log, name='login'),
    path('register/', views.regis, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('adminn/', views.adm, name='adm'),
    path('timer/', views.timer, name='timer'),
    path('about/', views.about, name='about'),
    path('course/', views.cou, name='course'),
    path('adminn/users/', views.users, name='users'),
    path('courses_admin/', views.cou_adm, name='cou_admin'),
    path('feedback_admin/', views.feedback_adm, name='feedback_admin'),
    path('profile/', views.prof, name='profile'),
    path('course/<int:course_id>/', views.detail, name='detail'),
    path('feedback/', views.feedback, name='feedback'),
    path('setting/', views.setting, name='setting'),
    path('useredit/<int:post_id>', views.update_users, name='user_edit'),
]   