from django.db import models

# Create your models here.
class Cliente(models.Model):
    iden = models.IntegerField(primary_key=True,unique=True,verbose_name="Identificacion",
    error_messages={'unique':'Ya existe un cliente registrado con este ID'})
    nombre = models.CharField(max_length=50,verbose_name="Nombre del Cliente")
    apellidos = models.CharField(max_length=50,verbose_name="Apellidos del cliente")
    direccion = models.CharField(max_length=100,verbose_name="Direccion de Residencia")
    correo = models.EmailField(max_length=254,verbose_name="Correo Electronico")
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s %s %s'%(self.iden,self.nombre,self.apellidos)

class Autor(models.Model):
    pseudonimo = models.CharField(max_length=50,verbose_name="Nombre del Autor",primary_key=True,unique=True,
    error_messages={'unique':'Ya existe un registro con este nombre'})
    direccion = models.CharField(max_length=100,verbose_name="Direccion de Residencia")
    correo = models.EmailField(max_length=254,verbose_name="Correo Electronico")
    bio = models.TextField(null = True, blank=True)
    

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return '%s'%(self.pseudonimo)


