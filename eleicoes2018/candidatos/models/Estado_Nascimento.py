from django.db import models

class Estado_Nascimento(models.Model):
    UF = models.CharField(max_length=3, help_text="Estado de origem do candidato", unique=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = "Estados"

    def __str__(self):
        return "%s" %(self.UF)
