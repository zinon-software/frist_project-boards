from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
# Register your models here.

admin.site.site_header = "Boards Admin Panel"
admin.site.site_title = 'Boards Admin Panel'

"""
class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]
"""
# كلاس لعرض عدد معين من العناصر
class TopicAdmin(admin.ModelAdmin):
    #  دالة التحكم بعدد العناصر المعروضة في صفحة التعديل
    # fields = ('subject', 'board', 'created_by', 'views')
    list_display = ('subject', 'board', 'created_by', 'views', 'combine_subject_and_board')
    list_display_links = ('board', 'created_by', 'views', 'combine_subject_and_board')
    list_editable = ('subject',)
    list_filter = ('board', 'created_by',)
    search_fields = ('board', 'created_by',)

    def combine_subject_and_board(self, obj):
        return "{} + {}".format(obj.subject, obj.board)

admin.site.register(Board) # , BoardAdmin
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post)

# دالة لعمل اخفاء ل جدول معين
# admin.site.unregister(Group)
