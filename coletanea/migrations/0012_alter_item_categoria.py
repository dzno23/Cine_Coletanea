# Generated by Django 4.0.4 on 2022-06-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletanea', '0011_alter_item_categoria_alter_item_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.CharField(choices=[('1', 'Ação'), ('2', 'Aventura'), ('3', 'Comédia')], default='', max_length=2),
        ),
    ]
