# Generated by Django 3.0.7 on 2020-08-23 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200823_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneta',
            name='autor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='awers',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Awers'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='cena',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena katalogowa w €'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='cenaz',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena zapłacona w zł'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='katalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Katalog', verbose_name='Do jakiego katalogu należy'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Material', verbose_name='Materiał'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='mennica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Mennica'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='opis',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='opis'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='panowanie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Krolowie'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='pochodzenie',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='rant',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='opis'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='rewers',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rewers'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='rok',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rok'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='rzadkosc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Rzadkosc'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='srednica',
            field=models.IntegerField(blank=True, null=True, verbose_name='Średnica w mm'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='stan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Stan'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='waga',
            field=models.FloatField(blank=True, null=True, verbose_name='Waga w gramach'),
        ),
    ]
