from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions/<int:pk>', views.QuestionView.as_view(), name='question'),
    path('questions', views.QuestionsView.as_view(), name='questions'),
]
