from django.contrib import admin

# Register your models here.
from.models import Zona, Departamento, Municipio, TipoEntidad, Entidad, TipoAyuda, Beneficiado, Ayuda

admin.site.register(Zona)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(TipoEntidad)
admin.site.register(Entidad)
admin.site.register(TipoAyuda)
admin.site.register(Beneficiado)
admin.site.register(Ayuda)
