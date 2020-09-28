from django.db import models

# Create your models here.
class Article(models.Model):
    # 텍스트
    content = models.CharField(max_length=150)
    # 글자 크기
    font_size = models.IntegerField()
    # 색상 코드
    color_code = models.CharField(max_length=10)
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 위와 간격
    top_gap = models.FloatField()
    # 왼쪽과 간격
    left_gap = models.FloatField()