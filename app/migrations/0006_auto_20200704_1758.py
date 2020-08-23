# Generated by Django 3.0.7 on 2020-07-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200704_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneta',
            old_name='ID',
            new_name='Nr',
        ),
        migrations.AlterField(
            model_name='dynastie',
            name='kpanowanie',
            field=models.DateTimeField(verbose_name='Data zakonczenia'),
        ),
        migrations.AlterField(
            model_name='dynastie',
            name='nazwa',
            field=models.CharField(max_length=70, verbose_name='Nazwa dynastii'),
        ),
        migrations.AlterField(
            model_name='dynastie',
            name='ppanowanie',
            field=models.DateTimeField(verbose_name='Data rozpoczecia'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='autor',
            field=models.CharField(max_length=70, null=True, verbose_name='autor'),
        ),
    ]