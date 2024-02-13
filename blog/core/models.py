from django.db import models

# Create your models here.
class Core(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linions = models.BooleanField(default=False)
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)

    class Meta:
        ordering=["created"]

    def __str__(self):
        return self.title