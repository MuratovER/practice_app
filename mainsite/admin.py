from django.contrib import admin
from mainsite.models import Post, Comment, CodeExamples, EulerProblem, Stock


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(CodeExamples)
admin.site.register(EulerProblem)
admin.site.register(Stock)
