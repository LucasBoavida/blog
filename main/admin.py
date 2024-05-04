from django.contrib import admin
from main.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#OINSA ATU EXPORT NO IMPORT DADOS SIRA

#Portfolio
class PorfolioResource(resources.ModelResource):
    class Meta:
        model = Porfolio

class PortfolioAdmin(ImportExportModelAdmin):
    resource_classes = [PorfolioResource]
admin.site.register(Porfolio,PortfolioAdmin)


#Categoria
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin):
    resource_classes = [CategoriaResource]
admin.site.register(Categoria,CategoriaAdmin)


#Project
class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project

class PortfolioAdmin(ImportExportModelAdmin):
    resource_classes = [ProjectResource]
admin.site.register(Project,PortfolioAdmin)


#Post
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_classes = [PostResource]
admin.site.register(Post,PostAdmin)
