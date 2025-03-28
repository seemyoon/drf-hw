from django.db import models
from core.models import BaseModel


class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza'

    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=20)
    weight = models.FloatField()
