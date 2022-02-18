# Generated by Django 3.2.8 on 2022-02-18 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0026_alter_portfolio_asset_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.FloatField(default=0)),
                ('percantage', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='asset_type',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stocks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.stock'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='deposit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.deposit'),
        ),
    ]