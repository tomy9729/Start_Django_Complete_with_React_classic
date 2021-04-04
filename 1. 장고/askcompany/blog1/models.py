from django.db import models

class Post(models.Model): #어떤 post를 저장
    title = models.CharField(max_length=100) #제목은 최대 100자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)#저장시간
    updated_at = models.DateTimeField(auto_now=True)#업데이트 시간
#위 구조로 데이터베이스에 저장되게 됩니다.