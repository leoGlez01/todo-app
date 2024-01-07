from django.db import models

class Task(models.Model):
    title = models.CharField(max_length = 50, null = False)
    body = models.TextField(max_length= 200, null =True, blank = True)
     
    objects = models.Manager() # The default manager.

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'Task'

    def __str__(self):
        return self.title