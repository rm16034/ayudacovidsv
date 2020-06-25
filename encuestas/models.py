from django.db import models

# Create your models here.
class Zona(models.Model):
    nombreZona=models.CharField(max_length=50)

class Departamento(models.Model):
    nombreDepartamento=models.CharField(max_length=50)
    codigoISO=models.CharField(max_length=6)
    idZona=models.ForeignKey('Zona', on_delete=models.CASCADE)

class Municipio(models.Model):
    nombreMunicipio=models.CharField(max_length=50)
    idDepartamento=models.ForeignKey('Departamento',on_delete=models.CASCADE)

class Beneficiado(models.Model):
    dui=models.CharField(max_length=9)
    idDepartamento=models.ForeignKey('Departamento',on_delete=models.CASCADE)
    idMunicipio=models.ForeignKey('Municipio',on_delete=models.CASCADE)

class TipoEntidad(models.Model):
    nombreTipoEntidad=models.CharField(max_length=50)
    sigla=models.CharField(max_length=10)

class Entidad(models.Model):
    nombreEntidad=models.CharField(max_length=100)
    idTipoEntidad=models.ForeignKey('TipoEntidad',on_delete=models.CASCADE)

class TipoAyuda(models.Model):
    nombreTipoAyuda=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=250)

class Ayuda(models.Model):
    idTipoEntidad=models.ForeignKey('TipoEntidad',on_delete=models.CASCADE)
    idEntidad=models.ForeignKey('Entidad',on_delete=models.CASCADE)
    idTipoAyuda=models.ForeignKey('TipoAyuda',on_delete=models.CASCADE)
    idBeneficiado=models.ForeignKey('Beneficiado',on_delete=models.CASCADE)
