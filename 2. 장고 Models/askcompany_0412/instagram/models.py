#instagram/models.py
from django.db import models

class Post(models.Model) : #원하는 설계에 맞춰 작성하면 된다.
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to = 'instagram/post/%Y/%m/%d') 
    #blank=True를 통해 photo를 옵션 필드로 설정할 수 있다.
    is_public = models.BooleanField(default=False, verbose_name="공개 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) : 
        #return f"My Post object ({self.id})"
        #return "My Post object ({})".format(self.id)
        return self.message

    # def message_length(self) : 
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"