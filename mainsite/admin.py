from django.contrib import admin
from mainsite.models import Post, Comment, CodeExamples, EulerProblem

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(CodeExamples)
admin.site.register(EulerProblem)