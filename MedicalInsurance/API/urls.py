from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questions',QuestionAPI)
urlpatterns = [
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view())
]
urlpatterns+= router.urls