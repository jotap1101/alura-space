from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'legenda', 'descricao', 'imagem', 'status', 'data_fotografia', 'user']
    list_display_links = ['id', 'nome']
    list_editable = ['status']
    list_filter = ['categoria', 'status', 'user']
    list_per_page = 10
    search_fields = ['nome']

admin.site.register(Fotografia, FotografiaAdmin)