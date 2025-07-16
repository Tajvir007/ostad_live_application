from django.db import models
from account.models import User

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_by = models.EmailField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modifyed_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:

        try:
            return self.name
        except:
            return super().__str__()