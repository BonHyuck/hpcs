from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
    # 글 작성 URL
    path('create/', views.create, name='create')
    # 글 삭제 및 수정 없음
]