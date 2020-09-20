from django.contrib import admin

from .models import Category, Task

# Register your models here.

def mark_all_tasks_done(ModelAdmin, request, queryset):
    queryset.update(status='OK')

mark_all_tasks_done.short_description = "Concluir Tarefas selecionadas"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['owner']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'end_date', 'status', 'list_categories']
    search_fields = ['name', 'description']
    list_filter = ['end_date', 'status']
    actions = [mark_all_tasks_done]

    def list_categories(self, obj):
        return ", ".join([c.name for c in obj.category.all()])

    list_categories.short_description = "Categorias"



#admin.site.register(Category, CategoryAdmin) outra opção

