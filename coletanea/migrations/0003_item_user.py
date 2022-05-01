# Generated by Django 4.0.4 on 2022-04-30 23:46

import ast
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coletanea', '0002_alter_capa_capa_alter_item_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=ast.Delete, to=settings.AUTH_USER_MODEL),
        ),
    ]
