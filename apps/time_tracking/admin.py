from django.contrib import admin

from .models import TimeRecord, TimeMainTopic, TimeSubTopic

# Register your models here.


class TimeMainTopicAdmin(admin.ModelAdmin):
    readonly_fields = ["color"]
    

admin.site.register(TimeMainTopic, TimeMainTopicAdmin)
admin.site.register(TimeRecord)
admin.site.register(TimeSubTopic)