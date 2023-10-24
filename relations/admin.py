from django.contrib import admin

from relations.models import Student, Teacher, Course, CourseStudent


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'id', 'first_name', 'age')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'id', 'first_name', 'age')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'course_id', 'date')

