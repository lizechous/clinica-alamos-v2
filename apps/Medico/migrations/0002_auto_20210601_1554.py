# Generated by Django 3.1.1 on 2021-06-01 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citamedica',
            name='nombre_medico',
        ),
        migrations.AddField(
            model_name='citamedica',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='Medico.medico'),
        ),
        migrations.AlterField(
            model_name='citamedica',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='citamedica',
            name='run',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medico',
            name='run_medico',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]