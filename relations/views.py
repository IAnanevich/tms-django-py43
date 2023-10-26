from django.urls import reverse
from django.views import generic

from relations.form import StudentForm
from relations.models import Student


class StudentsListView(generic.ListView):
    template_name = 'relations/relations_list.html'
    context_object_name = 'students'
    queryset = Student.objects.all()

    # select_related - O2O, O2M
    # prefetch_related - M2O, M2M

    # def get_queryset(self):
    #
    #     student = Student.objects.get(id=1)
    #     print(student.course)
    #
    #     return Student.objects.all()


class StudentsCreateView(generic.CreateView):
    template_name = 'relations/relations_create.html'
    form_class = StudentForm
    # extra_context = {'teachers': Teacher.objects.values_list('last_name', flat=True)}
    # fields = ('name', 'text', 'rating', 'price')
    # success_url = '/blog/posts/'

    # def form_valid(self, form):
        # result = super().form_valid(form)

        # CourseStudent.objects.create(, )

    def get_success_url(self):
        return reverse('students')



# class PostCreateView(generic.CreateView):
#     # model = InfoBlog
#     template_name = 'info_blog/post_create.html'
#     form_class = InfoBlogForm
#     # fields = ('name', 'text', 'rating', 'price')
#     # success_url = '/blog/posts/'
#
#     def get_success_url(self):
#         return reverse('post-list')
#
#
# class PostDetailView(generic.DetailView):
#     model = InfoBlog
#     template_name = 'info_blog/post_detail.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = InfoBlog.objects.filter(is_deleted=False)
#
#         return context
#
#
# class PostUpdateView(generic.UpdateView):
#     model = InfoBlog
#     template_name = 'info_blog/post_update.html'
#     form_class = InfoBlogForm
#
#     def get_success_url(self):
#         return reverse('post-list')
#
#
# class PostDeleteView(generic.DeleteView):
#     pass
