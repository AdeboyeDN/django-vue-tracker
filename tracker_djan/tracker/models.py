from django.db import models

class task(models.Model):
     title = models.CharField(max_length=500, blank=False, null=False)
     done = models.BooleanField(default=False),
     date = models.DateTimeField(auto_now_add=True, )

     def __str__(self):
         return self.title

     class Meta:
          ordering = ['-date']

     