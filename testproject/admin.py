from django.contrib import admin
from aws_manager.models import AWSServer
from aws_manager.admin import AWSServerAdmin

admin.site.register(AWSServer, AWSServerAdmin)


