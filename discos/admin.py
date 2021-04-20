from django.contrib import admin
from .models import Tamanho, Vinil, Capa, Disco


class DiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'artista', 'album', 'pais', 'gravadora', 'lancamento', 'cor',
                    'tamanho', 'vinil', 'capa')

    list_display_links = ('id', 'artista', 'album')

    list_per_page = 10


admin.site.register(Tamanho)
admin.site.register(Vinil)
admin.site.register(Capa)
admin.site.register(Disco, DiscoAdmin)
