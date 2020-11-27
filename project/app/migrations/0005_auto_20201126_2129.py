# Generated by Django 3.1.3 on 2020-11-27 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201126_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structuredfinancialinvestment',
            name='fp_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.financialproduct'),
        ),
        migrations.AlterField(
            model_name='structuredfinancialinvestment',
            name='stock_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.stockinfo'),
        ),
    ]
