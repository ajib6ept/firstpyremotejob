from django.db import models


class SourceRemoteJob(models.Model):

    NAME_LENGTH = 100

    name = models.CharField(max_length=NAME_LENGTH)

    def __str__(self):
        """Represent an instance as a string."""
        return self.name


class RemoteJob(models.Model):

    TITLE_LENGTH = 100
    SALARY_LENGHT = 100

    title = models.CharField(max_length=TITLE_LENGTH)
    url = models.URLField()
    source = models.ForeignKey(SourceRemoteJob, on_delete=models.CASCADE)
    salary = models.CharField(max_length=SALARY_LENGHT)
    publication_date = models.DateField()

    def __str__(self):
        """Represent an instance as a string."""
        return self.title
