from django.contrib import admin
from .models import QuestionMainTopic, QuestionRecord, QuestionSubTopic

# Register your models here.


class QuestionMainTopicAdmin(admin.ModelAdmin):
    readonly_fields = ["color"]
    

admin.site.register(QuestionMainTopic, QuestionMainTopicAdmin)
admin.site.register(QuestionRecord)
admin.site.register(QuestionSubTopic)