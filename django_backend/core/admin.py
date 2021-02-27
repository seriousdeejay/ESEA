from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (CustomUser, Network, Organisation, UserOrganisation, Method, Topic, DirectIndicator, Question, QuestionOption)

class NetworkAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by']
    
    def get_form(self, request, obj=None, **kwargs):
        Network.created_by = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.created_by_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Organisation)
admin.site.register(UserOrganisation)
admin.site.register(Method)
admin.site.register(Topic)
admin.site.register(DirectIndicator)
admin.site.register(Question)
admin.site.register(QuestionOption)
# admin.site.register(IndirectIndicator)