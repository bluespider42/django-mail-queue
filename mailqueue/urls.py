from django.urls import path
from . import views

urlpatterns = [
    path('clear/', views.clear_sent_messages, name='clear_sent_messages'),
    path('/', views.run_mail_job, name='run_mail_job'),
]
