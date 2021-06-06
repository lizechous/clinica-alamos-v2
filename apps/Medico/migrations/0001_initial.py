# Generated by Django 3.1.3 on 2021-06-01 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.TextField()),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('run_medico', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_medico', models.TextField()),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medico.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('run', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_paciente', models.TextField()),
                ('tipo_prevision', models.CharField(choices=[('Fonasa', 'Fonasa'), ('Isapre', 'Isapre'), ('Ninguna', 'Ninguna')], max_length=50)),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.TimeField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='especialidad', to='Medico.especialidad')),
                ('nombre_medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medico.medico')),
            ],
        ),
    ]
