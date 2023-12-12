from django.contrib import admin
from .models import User, Candidate, Recruiter, Job, Application, Message

# Register your models here.

admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Message)