# Generated by Django 5.0.4 on 2024-08-09 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uno', '0002_comentario_nombre_alter_trabajador_descripción'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comentario',
            name='calificación',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='uno.calificación'),
            preserve_default=False,
        ),
    ]
