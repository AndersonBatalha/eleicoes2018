from django.db import models


class Cargo(models.Model):
    desc_cargo = models.CharField(max_length=100, help_text="Cargo pelo qual o candidato está concorrendo", unique=True)

    class Meta:
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.desc_cargo