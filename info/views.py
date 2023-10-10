from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from info.models import InfoBlog


# Create your views here.

def read_post(request):
    # if request.method == 'GET':
    #     return render(request, 'index.html')
    # elif request.method == 'POST':
    return render(request, 'index.html')


class PostsView(View):
    def get(self, request, id=None):
        posts = InfoBlog.objects.filter(is_deleted=False)

        if id:
            post = InfoBlog.objects.filter(id=id, is_deleted=False).first()
            return render(request, 'post.html', context={'post': post, 'posts': posts})

        return render(request, 'index.html', context={'posts': posts})
