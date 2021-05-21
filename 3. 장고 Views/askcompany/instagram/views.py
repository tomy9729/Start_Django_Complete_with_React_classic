#instagram/views.py
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic.dates import YearArchiveView
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#post_list = login_required(ListView.as_view(model=Post, paginate_by=3))

@method_decorator(login_required, name='dispatch')
class PostListView(ListView) : 
    model = Post
    paginate_by = 3

post_list = PostListView.as_view()

# @login_required
# def post_list(request) : #호출 당시에 모든 인자를 전달 받음
#      qs = Post.objects.all() #사용할 쿼리문을 만들 준비
#      q = request.GET.get('q', '') # q라는 인자가 있으면 받아오고 없다면 빈문자열을 받음
#      if q : 
#          qs = qs.filter(message__icontains=q) # q가 존재한다면 쿼리문 생성
#      return render(request,'instagram/post_list.html',{ #instagram/templates/instagram/post_list.html
#          'post_list' : qs,
#          'q':q,
#      }) # render를 통해 손쉽게 html문자열을 조합

#def post_detail(request, pk) : 
    #post = get_object_or_404(Post, pk=pk)
    #try : 
    #    post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist : 
    #    raise Http404
    #return render(request,'instagram/post_detail.html',{
    #    'post':post,
    #})
#post_detail = DetailView.as_view(model=Post)

class PostDetailView(DetailView)  :
    model = Post
    def get_queryset(self) :
        qs = super().get_queryset() # DetailView의 get_queryser() 함수
        if not self.request.user.is_authenticated: # 만약 로그인되지 않은 사용자라면 
            qs = qs.filter(is_public = True) #qs를 is_ppublic = True로 필터링
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request,year) : 
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by = 3)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list = True)