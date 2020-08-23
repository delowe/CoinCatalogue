# Generated by Django 3.0.7 on 2020-07-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200704_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneta',
            name='katalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Katalog', verbose_name='Do jakiego katalogu należy'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Material', verbose_name='Materiał'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='mennica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Mennica'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='panowanie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Krolowie'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='rzadkosc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Rzadkosc'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='srednica',
            field=models.IntegerField(null=True, verbose_name='Średnica w mm'),
        ),
        migrations.AlterField(
            model_name='moneta',
            name='stan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Stan'),
        ),
    ]
