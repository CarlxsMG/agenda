# Django imports
from django.db import models
from django.db.models import Count


class ReunionManager(models.Manager):

    def cantidad_reuniones_job(self):
        result = self.values('persona__job').annotate(
            cantidad=Count('id')
        )

        return result