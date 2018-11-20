from django.db import models


class Cargo(models.Model):
    desc_cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.desc_cargo