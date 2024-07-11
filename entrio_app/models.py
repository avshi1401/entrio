from django.db import models


class Repositories(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column="NAME", max_length=50, blank=False, null=False)
    id = models.IntegerField(db_column="ID", blank=False, null=False)
    stars = models.IntegerField(db_column="STARS", blank=False, null=True)
    owner = models.CharField(db_column="OWNER", max_length=50, blank=False, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=False, null=True)
    forks = models.JSONField(db_column="FORKS", blank=False, null=True)
    languages = models.JSONField(db_column="LANGUAGES", blank=False, null=True)
    number_of_forks = models.IntegerField(db_column="NUMBER_OF_FORKS", blank=False, null=True)
    topics = models.JSONField(db_column="TOPICS", blank=False, null=True)

    class Meta:
        managed = True
        db_table = "repositories"
