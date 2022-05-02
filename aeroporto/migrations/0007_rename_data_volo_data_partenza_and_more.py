# Generated by Django 4.0.3 on 2022-04-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeroporto', '0006_alter_personale_codice_personale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volo',
            old_name='data',
            new_name='data_partenza',
        ),
        migrations.RenameField(
            model_name='volo',
            old_name='orario',
            new_name='orario_partenza',
        ),
        migrations.AddField(
            model_name='volo',
            name='data_arrivo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volo',
            name='durata_volo',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='volo',
            name='orario_arrivo',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
