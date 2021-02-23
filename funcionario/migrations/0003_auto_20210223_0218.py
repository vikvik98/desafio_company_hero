# Generated by Django 3.1.7 on 2021-02-23 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionario', '0002_auto_20210223_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuario_django',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
        ),
    ]
