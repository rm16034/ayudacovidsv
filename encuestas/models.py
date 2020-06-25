from django.db import models

# Create your models here.

#Modelo de Zona (Occidental, Central, Paracentral, Oriental)
class Zona(models.Model):
    nombreZona=models.CharField(max_length=50)

    def __str__(self):
        return self.nombreZona
 
#Modelo de Departamentos, los 14 del pais
class Departamento(models.Model):
    nombreDepartamento=models.CharField(max_length=50)
    codigoISO=models.CharField(max_length=6)
    zona=models.ForeignKey('Zona', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreDepartamento

#Modelo de Municipio, los 262 del pais asociados con su respectivo departamento
class Municipio(models.Model):
    nombreMunicipio=models.CharField(max_length=50)
    departamento=models.ForeignKey('Departamento',on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMunicipio

#Modelo de Beneficiado, los datos que se le pediran
class Beneficiado(models.Model):
    dui=models.CharField(max_length=9)
    departamento=models.ForeignKey('Departamento',on_delete=models.CASCADE)
    municipio=models.ForeignKey('Municipio',on_delete=models.CASCADE)

#Modelo de TipoEntidad (Gubernamental, ONG, Particulares, etc)
class TipoEntidad(models.Model):
    nombreTipoEntidad=models.CharField(max_length=50)
    sigla=models.CharField(max_length=10)

#Modelo Entidad (Si se selecciona cualquiera que no sea ayuda particular especificar quien hizo ayuda)
class Entidad(models.Model):
    nombreEntidad=models.CharField(max_length=100)
    tipoEntidad=models.ForeignKey('TipoEntidad',on_delete=models.CASCADE)

#Modelo Tipo Ayuda, si fue monetaria, canasta basica, ropa, etc
class TipoAyuda(models.Model):
    nombreTipoAyuda=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=250)

#Modelo Ayuda, la que asocia casi todo lo anterior
class Ayuda(models.Model):
    tipoEntidad=models.ForeignKey('TipoEntidad',on_delete=models.CASCADE)
    entidad=models.ForeignKey('Entidad',on_delete=models.CASCADE)
    iipoAyuda=models.ForeignKey('TipoAyuda',on_delete=models.CASCADE)
    beneficiado=models.ForeignKey('Beneficiado',on_delete=models.CASCADE)
