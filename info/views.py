from django.shortcuts import render
from django.views import generic

from info.models import InfoBlog


# Create your views here.
def read_post(request):
    # if request.method == 'GET':
    #     return render(request, 'index.html')
    # elif request.method == 'POST':
    return render(request, 'index.html')


# class PostsView(View):
#     def get(self, request, id=None):
#         posts = InfoBlog.objects.filter(is_deleted=False)
#
#         if id:
#             post = InfoBlog.objects.filter(id=id, is_deleted=False).first()
#             return render(request, 'post.html', context={'post': post, 'posts': posts})
#
#         return render(request, 'index.html', context={'posts': posts})


class PostListView(generic.ListView):
    # model = InfoBlog
    template_name = 'info_blog/post_list.html'
    context_object_name = 'posts'
    queryset = InfoBlog.objects.filter(is_deleted=False)
    # ordering = 'price'

    # def get_queryset(self):
    #     email = self.request.GET.get('email')
    #     print(email)
    #     return InfoBlog.objects.filter(email=email)


class PostCreateView(generic.CreateView):
    pass


class PostDetailView(generic.DetailView):
    model = InfoBlog
    template_name = 'info_blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = InfoBlog.objects.filter(is_deleted=False)
        return context


class PostUpdateView(generic.UpdateView):
    pass


class PostDeleteView(generic.DeleteView):
    pass
