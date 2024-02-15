from django.contrib import admin

# Register your models here.
from .models import Educator
from .models import Course

admin.site.register(Educator)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Include existing attributes
    list_filter = ('difficulty',)
    def get_instructor(self, obj):
        return obj.instructor  # Replace 'instructor' with the actual field name
    get_instructor.short_description = 'Instructor'
admin.site.register(Course, CourseAdmin)

