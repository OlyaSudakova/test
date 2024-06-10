
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from user.views import register, profile, profileedit

urlpatterns = [
    path('catalog/', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration', register, name='registration'),
    path('profile', profile, name='profile'),
    path('profileedit', profileedit, name='profileedit'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main.html'), name='logout'),

    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('faq', views.faq, name='faq'),
    path('news', views.news, name='news'),
    path('discounts', views.discount, name='discounts'),
    path('requestImm', views.offersImm, name='requestImm'),
    path('requestRent', views.offersRent, name='requestRent'),
    path('policy', views.policy, name='policy'),
    path('doctors', views.doctors, name='doctors'),
    path('time', views.userTime, name='time'),
    path('employee', views.employee, name='employee'),
    path('vacancies', views.vacancies, name='vacancies'),

]