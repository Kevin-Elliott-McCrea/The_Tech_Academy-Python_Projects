from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=255)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=255)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title


calculus = djangoClasses.objects.update_or_create(title="Calculus 101", courseNumber=1, instructorName="Jim", duration=40)

history = djangoClasses.objects.update_or_create(title="History of Man", courseNumber=2, instructorName="Ernie", duration=40)

grammar = djangoClasses.objects.update_or_create(title="Grammar for Dummies", courseNumber=3, instructorName="Sandy", duration=40)


