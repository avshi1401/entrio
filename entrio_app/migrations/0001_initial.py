# Generated by Django 5.0.6 on 2024-07-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=50)),
                ('id', models.IntegerField(db_column='ID')),
                ('stars', models.IntegerField(db_column='STARS', null=True)),
                ('owner', models.CharField(db_column='OWNER', max_length=50, null=True)),
                ('description', models.TextField(db_column='DESCRIPTION', null=True)),
                ('forks', models.JSONField(db_column='FORKS', null=True)),
                ('languages', models.JSONField(db_column='LANGUAGES', null=True)),
                ('number_of_forks', models.IntegerField(db_column='NUMBER_OF_FORKS', null=True)),
                ('topics', models.JSONField(db_column='TOPICS', null=True)),
            ],
            options={
                'db_table': 'repositories',
                'managed': True,
            },
        ),
    ]
