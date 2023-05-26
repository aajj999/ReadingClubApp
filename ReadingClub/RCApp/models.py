from django.db import models

class Author(models.Model):
   name = models.CharField(max_length=100)

class Type(models.Model):
   typeName = models.CharField(max_length=100, unique = True)

   @classmethod
   def getDefaultPk(cls):
      type, created = cls.objects.get_or_create(
         defaults=dict(typeName='type not chosen'),
      )
      return type.pk

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
   type = models.ForeignKey(Type, on_delete=models.CASCADE, default=Type.getDefaultPk)