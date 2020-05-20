from django.contrib.postgres.fields import ArrayField
from django.db import models

from main_app.models import CustomBaseModel


class Genre(CustomBaseModel):
    mass_office_choices = [
        ("Mass", "Mass"),
        ("Office", "Office"),
        ("Hispanic", "Old Hispanic"),
    ]
    name = models.CharField()
    description = models.TextField()
    mass_office = ArrayField(
        base_field=models.CharField(choices=mass_office_choices, max_length=8), size=3
    )
