from django.contrib import admin
from .models import InsecureUser, Product, Comment, HazMat

admin.site.register(InsecureUser)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(HazMat)
