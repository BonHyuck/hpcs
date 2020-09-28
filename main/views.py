from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Article
import random

# Create your views here.
# 메인페이지
def index(request, *something):
    articles = Article.objects.all()
    print(something)
    context = {
        'articles':articles,
    }
    return render(request, 'main/index.html', context)

# 글 생성
# @require_POST
def create(request):
    if request.method == 'POST':
        article = Article()
        if 0 < len(request.POST['content']) <= 100:
            article.content = request.POST['content']
        if 0 < int(request.POST['font_size']) <= 50:
            article.font_size = request.POST['font_size']
        if '#' in request.POST['color_code'] and len(request.POST['color_code']) == 7:
            article.color_code = request.POST['color_code']
        if article.content == request.POST['content'] and article.font_size == request.POST['font_size'] and article.color_code == request.POST['color_code']:
            article.top_gap = random.random() * 100
            article.left_gap = random.random() * 100
            article.save()
    # Article.objects.all().delete()        
    return redirect('main:index')
# 글 수정, 삭제 없음. 조회는 index에서 구현