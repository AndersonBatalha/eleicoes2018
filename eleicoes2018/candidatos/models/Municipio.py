from django.db import models


class Municipio(models.Model):
    municipio = models.CharField(max_length=75)

    def __str__(self):
        return self.municipio