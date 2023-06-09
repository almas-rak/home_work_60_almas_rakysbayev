# Generated by Django 4.1.5 on 2023-03-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='Дата и время удаления'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False, null=True, verbose_name='Удалено'),
        ),
    ]
