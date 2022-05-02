# Generated by Django 4.0.3 on 2022-04-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aeroporto', '0003_alter_aeroporto_iata_code_alter_aeroporto_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volo',
            name='aeromobile',
        ),
        migrations.RemoveField(
            model_name='volo',
            name='distanza',
        ),
        migrations.RemoveField(
            model_name='volo',
            name='operatore',
        ),
        migrations.RemoveField(
            model_name='volo',
            name='ora_arrivo',
        ),
        migrations.RemoveField(
            model_name='volo',
            name='ora_partenza',
        ),
        migrations.RemoveField(
            model_name='volo',
            name='scheduling',
        ),
        migrations.AddField(
            model_name='volo',
            name='aereo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aeroporto.aeromobile'),
        ),
        migrations.AddField(
            model_name='volo',
            name='andata_ritorno',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volo',
            name='arrivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aeroporto_di_arrivo', to='aeroporto.aeroporto'),
        ),
        migrations.AddField(
            model_name='volo',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volo',
            name='orario',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volo',
            name='partenza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aeroporto_di_partenza', to='aeroporto.aeroporto'),
        ),
        migrations.AddField(
            model_name='volo',
            name='posti_disponibili',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='volo',
            name='posti_prenotati',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='volo',
            name='sola_andata',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volo',
            name='solo_ritorno',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aeromobile',
            name='codice',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aeromobile',
            name='modello',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aeroporto',
            name='continent',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aeroporto',
            name='gps_code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aeroporto',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aeroporto',
            name='type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='volo',
            name='aeroporto_arrivo',
            field=models.CharField(max_length=199),
        ),
        migrations.AlterField(
            model_name='volo',
            name='aeroporto_partenza',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='volo',
            name='codice_volo',
            field=models.CharField(max_length=200),
        ),
    ]
