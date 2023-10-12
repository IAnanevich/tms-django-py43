from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from info.form import InfoBlogForm
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
    # model = InfoBlog
    template_name = 'info_blog/post_create.html'
    form_class = InfoBlogForm
    # fields = ('name', 'text', 'rating', 'price')
    # success_url = '/blog/posts/'

    def get_success_url(self):
        return reverse('post-list')


class PostDetailView(generic.DetailView):
    model = InfoBlog
    template_name = 'info_blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = InfoBlog.objects.filter(is_deleted=False)
        # print(50*'-')
        # print(context['posts'].values()[0]['name'])
        # print(context['posts'].query)
        # print(50*'-')
        return context


class PostUpdateView(generic.UpdateView):
    model = InfoBlog
    template_name = 'info_blog/post_update.html'
    form_class = InfoBlogForm

    def get_success_url(self):
        return reverse('post-list')


class PostDeleteView(generic.DeleteView):
    pass
